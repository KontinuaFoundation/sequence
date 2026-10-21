import numpy as np
from PIL import Image

# A 10 by 10 bitmap: 0 is black, 1 is white.
# The decimal points make these floating-point numbers.
bitmap = np.array([
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 1., 1., 1., 1., 1.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 1., 1., 1., 1., 1.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.]])

def show(array):
    # Scale 0-1 up to 0-255, convert to bytes, and enlarge 20x so you can see it
    pixels = (array * 255).astype(np.uint8)
    Image.fromarray(pixels).resize((200, 200), Image.NEAREST).show()

show(bitmap)              # the original
show(bitmap.transpose())  # rows become columns
show(np.rot90(bitmap))    # rotated 90 degrees counterclockwise
show(np.flipud(bitmap))   # flipped upside down
show(1.0 - bitmap)        # inverted: black becomes white
