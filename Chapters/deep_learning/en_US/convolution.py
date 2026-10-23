import numpy as np
from scipy.signal import correlate2d

# A 5 x 6 grayscale "image": dark on the left, bright on the right
image = np.array([[0, 0, 0, 9, 9, 9],
                  [0, 0, 0, 9, 9, 9],
                  [0, 0, 0, 9, 9, 9],
                  [0, 0, 0, 9, 9, 9],
                  [0, 0, 0, 9, 9, 9]])

# A 3 x 3 filter that responds to a change from left to right
vertical_edge = np.array([[-1, 0, 1],
                          [-1, 0, 1],
                          [-1, 0, 1]])

# Slide the filter over every 3 x 3 patch; each output is a sum of products
print(correlate2d(image, vertical_edge, mode="valid"))

horizontal_edge = vertical_edge.T
print(correlate2d(image, horizontal_edge, mode="valid"))
