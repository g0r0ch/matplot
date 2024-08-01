import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter, ScalarFormatter, FixedFormatter


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x) * 1e5)

# ax.set_xticklabels([])
# ax.set_yticklabels([])
# hide
# ax.xaxis.set_major_formatter(NullFormatter())
# ax.yaxis.set_major_formatter(NullFormatter())
# int
# ax.xaxis.set_major_formatter(NullFormatter())
# ax.yaxis.set_major_formatter(FormatStrFormatter("%d"))
# float
# ax.yaxis.set_major_formatter(FormatStrFormatter("%f"))
# float round
# ax.yaxis.set_major_formatter(FormatStrFormatter("name = %.2f"))
# func
# def format11(x, pos):
#     return f"[{x}]" if x < 0 else f"({x})"
#
# ax.yaxis.set_major_formatter(FuncFormatter(format11))

# for each plots

# sf = ScalarFormatter()
# sf.set_powerlimits((-4, 4))
# ax.yaxis.set_major_formatter(sf)

# for all plots

# matplotlib.rcParams["axes.formatter.limits"] = (-4, 4)

# ax.xaxis.set_major_formatter(FixedFormatter([-3, -2, -1, 0, 1, 2, 3]))

ax.xaxis.set_major_formatter(FixedFormatter(['a', 'b', 'c', 'd', 'e', 'f', 'g']))

ax.grid()
plt.show()