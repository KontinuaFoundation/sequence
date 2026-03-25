import numpy as np
# Father and son heights in inches
x = [66, 66, 67, 67, 68, 68, 69, 70, 71, 73]
y = [66, 65, 67, 70, 67, 70, 70, 72, 72, 74]
r = np.corrcoef(x, y)[0, 1]
print(r)
