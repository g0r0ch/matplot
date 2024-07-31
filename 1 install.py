# pip install matplotlib

import matplotlib
import matplotlib.pyplot as plt

#check Backend gtk... is interactive backend.
# print(matplotlib.get_backend())

plt.plot([1, 2, -6, 0, 4])
plt.show()

# base graph elements:

# Figure(aka canvas)
# Axes
# Grid
# x_min x_max X axis label
# y_min y_max Y axis label
# Legend