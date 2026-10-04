"""Generate the statistical tables for the stat_tables chapter.

Writes three LaTeX snippets (z_table.tex, t_table.tex, chi_table.tex) in the
same style as the chi-square chapter: table[H] + tabular + \\hline.
Every value is computed with scipy.stats, so rerunning the script
reproduces the tables exactly.

Usage: python gen_tables.py
"""
from scipy import stats

# Tail probabilities used on the AP Statistics formula sheet (Tables B and C)
TAILS = [0.25, 0.20, 0.15, 0.10, 0.05, 0.025, 0.02, 0.01, 0.005, 0.0025, 0.001, 0.0005]
T_DF = list(range(1, 31)) + [40, 50, 60, 80, 100, 1000, None]   # None = infinity
CHI_DF = list(range(1, 31)) + [40, 50, 60, 80, 100]


def p_label(p):
    txt = f"{p:.4f}".rstrip("0")
    if len(txt.split(".")[1]) < 2:
        txt += "0"
    return txt.lstrip("0")


def z_half(negative):
    rows = range(34, -1, -1) if negative else range(0, 35)
    cols = " & ".join(f".0{j}" for j in range(10))
    sign = "-" if negative else ""
    which = "negative" if negative else "positive"
    out = [
        r"\begin{table}[H]",
        r"\centering",
        r"\small",
        rf"\caption{{Standard normal cumulative probabilities, $P(Z \le z)$, {which} $z$}}",
        rf"\label{{tab:z-{which}}}",
        r"\begin{tabular}{c|cccccccccc}",
        rf"$z$ & {cols} \\",
        r"\hline",
    ]
    for r in rows:
        base = r / 10
        vals = []
        for j in range(10):
            z = -(base + j / 100) if negative else base + j / 100
            vals.append(f"{stats.norm.cdf(z):.4f}")
        out.append(f"${sign}{base:.1f}$ & " + " & ".join(vals) + r" \\")
    out += [r"\end{tabular}", r"\end{table}"]
    return "\n".join(out)


def t_table():
    head = " & ".join(p_label(p) for p in TAILS)
    conf = " & ".join(f"{100 * (1 - 2 * p):g}\\%" for p in TAILS)
    out = [
        r"\begin{table}[H]",
        r"\centering",
        r"\footnotesize",
        r"\setlength{\tabcolsep}{3.5pt}",
        r"\caption{$t$ distribution critical values, $t^*$ with upper-tail probability $p$}",
        r"\label{tab:t-critical}",
        r"\begin{tabular}{c|cccccccccccc}",
        rf" & \multicolumn{{12}}{{c}}{{Tail probability $p$}} \\",
        rf"$df$ & {head} \\",
        r"\hline",
    ]
    for df in T_DF:
        if df is None:
            vals = [stats.norm.isf(p) for p in TAILS]
            lab = r"$\infty$"
        else:
            vals = [stats.t.isf(p, df) for p in TAILS]
            lab = str(df)
        out.append(lab + " & " + " & ".join(f"{v:.3f}" for v in vals) + r" \\")
    out += [
        r"\hline",
        rf" & {conf} \\",
        rf" & \multicolumn{{12}}{{c}}{{Confidence level $C$}} \\",
        r"\end{tabular}",
        r"\end{table}",
    ]
    return "\n".join(out)


def chi_table():
    head = " & ".join(p_label(p) for p in TAILS)
    out = [
        r"\begin{table}[H]",
        r"\centering",
        r"\footnotesize",
        r"\setlength{\tabcolsep}{3.5pt}",
        r"\caption{Chi-square critical values, $\chi^2$ with upper-tail probability $p$}",
        r"\label{tab:chisq-full}",
        r"\begin{tabular}{c|cccccccccccc}",
        rf" & \multicolumn{{12}}{{c}}{{Tail probability $p$}} \\",
        rf"$df$ & {head} \\",
        r"\hline",
    ]
    for df in CHI_DF:
        vals = [stats.chi2.isf(p, df) for p in TAILS]
        out.append(f"{df} & " + " & ".join(f"{v:.3f}" for v in vals) + r" \\")
    out += [r"\end{tabular}", r"\end{table}"]
    return "\n".join(out)


if __name__ == "__main__":
    with open("z_table.tex", "w") as f:
        f.write(z_half(True) + "\n\n" + z_half(False) + "\n")
    with open("t_table.tex", "w") as f:
        f.write(t_table() + "\n")
    with open("chi_table.tex", "w") as f:
        f.write(chi_table() + "\n")
    print("Wrote z_table.tex, t_table.tex, chi_table.tex")
