import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator, LogLocator, MaxNLocator

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
# ax.plot(np.arange(1, 5, 0.25))

x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))

# ax.set(xlim=(-5, 30), ylim=(-1, 6))
# lc = NullLocator()
# ax.set_xlim(xmin=-5, xmax=10)
# ax.set_ylim(-1, 6)

ax.grid()
# ax.xaxis.set_major_locator(lc)
# ax.yaxis.set_major_locator(lc)
# ax.yaxis.set_major_locator(LinearLocator(5))
# ax.xaxis.set_major_locator(MultipleLocator(base=1))

# ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0.57))
# ax.xaxis.set_major_locator(FixedLocator([-2, -1, 0, 1, 2, 3]))
# ax.xaxis.set_major_locator(LogLocator(base=2))
# ax.xaxis.set_major_locator(MaxNLocator(5))
ax.minorticks_on()
ax.grid(which='major', lw = 2)
ax.grid(which='minor')


ax.xaxis.set_minor_locator(NullLocator())


plt.show()