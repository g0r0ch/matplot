import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import *

#line sample
# l1 = Line2D([1, 2, 3], [1, 2, 3])

#cos sample

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
cos = Line2D(x, np.cos(x))

#rect sample

rect = Rectangle((0, 0), 2.5, 0.5, facecolor='g')

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
# line_1, = ax.plot(np.arange(0, 5, 0.25), '--o', label='line_1')
# line_2 = ax.plot(np.arange(0, 10, 0.5), ':s', label='line_2')

# ax.legend((line_1, line_2), ['Line_1', 'Line_2'], loc='upper right') # or instead "loc='upper right')" bbox_to_anchor=(0.5, 0.7)

# ax.legend((line_1, line_2), [r'$f(x) = a \cdot b + c$', r'$f(x) = k \cdot x + b$'], facecolor='#aaa', framealpha=0.5)

ax.add_line(cos)
ax.add_patch(rect)
ax.set(xlim=(-2*np.pi, 2*np.pi), ylim=(-1, 1))
plt.show()