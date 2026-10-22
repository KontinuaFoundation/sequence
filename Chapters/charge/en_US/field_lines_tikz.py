# Author tool: generates the TikZ code for the electric field diagrams in student.tex.
# Run it, then paste pos.tex, neg.tex, and dip.tex into the figures.

import math
def fmt(p): return f"({p[0]:.2f},{p[1]:.2f})"
def radial(sign, R=6, n=16):
    out=[]
    for k in range(n):
        a=2*math.pi*k/n; c,s=math.cos(a),math.sin(a)
        out.append(f"\\draw[red, thin] ({0.35*c:.2f},{0.35*s:.2f}) -- ({9*c:.2f},{9*s:.2f});")
        r0,r1=(2.6,3.4) if sign>0 else (3.4,2.6)
        out.append(f"\\draw[red, -{{Stealth[length=5pt]}}] ({r0*c:.2f},{r0*s:.2f}) -- ({r1*c:.2f},{r1*s:.2f});")
    fill="white" if sign>0 else "black"
    out.append(f"\\filldraw[fill={fill}, draw=black, thick] (0,0) circle (0.3);")
    return out
def E(x,y,charges):
    ex=ey=0
    for q,cx,cy in charges:
        dx,dy=x-cx,y-cy; r3=(dx*dx+dy*dy)**1.5
        ex+=q*dx/r3; ey+=q*dy/r3
    return ex,ey
def trace(x,y,ch,sgn,box):
    pts=[(x,y)]; h=0.01
    for step in range(4000):
        ex,ey=E(x,y,ch); m=math.hypot(ex,ey); ex,ey=sgn*ex/m,sgn*ey/m
        mx,my=x+h/2*ex,y+h/2*ey
        ex2,ey2=E(mx,my,ch); m2=math.hypot(ex2,ey2)
        x,y=x+sgn*h*ex2/m2,y+sgn*h*ey2/m2
        pts.append((x,y))
        if math.hypot(x-1,y)<0.12 or math.hypot(x+1,y)<0.12 or abs(x)>box or abs(y)>box: break
    return pts
def dipole(n=16, box=3.6):
    ch=[(1,-1,0),(-1,1,0)]
    out=[]
    paths=[]
    for k in range(n):
        a=2*math.pi*k/n
        paths.append(trace(-1+0.12*math.cos(a),0.12*math.sin(a),ch,1,box))
        # lines into the negative charge that come from outside the frame (traced backward)
        b=trace(1+0.12*math.cos(a),0.12*math.sin(a),ch,-1,box)
        if math.hypot(b[-1][0]+1,b[-1][1])>0.2: paths.append(b[::-1])
    for pts in paths:
        pts=pts[::8]+[pts[-1]]
        out.append("\\draw[red, thin] plot[smooth] coordinates {"+" ".join(fmt(p) for p in pts)+"};")
        # arrow at the point of the path closest to halfway (by length)
        L=[0]
        for p,q in zip(pts,pts[1:]): L.append(L[-1]+math.dist(p,q))
        j=min(range(len(pts)-1),key=lambda i:abs(L[i]-min(L[-1]/2,1.5)))
        p,q=pts[j],pts[j+1]
        if abs(p[0])<3 and abs(p[1])<3:
            out.append(f"\\draw[red, -{{Stealth[length=5pt]}}] {fmt(p)} -- {fmt(q)};")
    out.append("\\filldraw[fill=white, draw=black, thick] (-1,0) circle (0.15);")
    out.append("\\filldraw[fill=black, draw=black, thick] (1,0) circle (0.15);")
    return out
def picture(lines, R, unit):
    return "\n".join([f"\\begin{{tikzpicture}}[x={unit}cm, y={unit}cm]",
        f"\\clip (-{R},-{R}) rectangle ({R},{R});",
        f"\\draw[gray!60, dotted] (-{R},-{R}) grid ({R},{R});",
        *lines, "\\end{tikzpicture}"])
open('pos.tex','w').write(picture(radial(+1),6,0.4))
open('neg.tex','w').write(picture(radial(-1),6,0.4))
open('dip.tex','w').write(picture(dipole(),3,1))
