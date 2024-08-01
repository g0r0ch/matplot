import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()
# step
# x = np.arange(0, 10)
# # ax.step(x, x, '-go')
# ax.step(x, x, '-go', where='post')

# stack

# x = np.arange(-2, 2, 0.1)
# y1 = np.array([-y**2 for y in x]) + 8
# y2 = np.array([-y**2 for y in x]) + 8
# y3 = np.array([-y**2 for y in x]) + 8
#
# ax.stackplot(x, y1, y2, y3)


# stem

# x = np.arange(-np.pi, np.pi, 0.3)
#
# ax.stem(x, np.cos(x), bottom=0.5)

# scatter

x = np.random.normal(0, 2, 500)
y = np.random.normal(0, 2, 500)

ax.scatter(x,y, s=50, c='g', linewidths=1, marker='s', edgecolors='r')

ax.grid()

plt.show()