import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# plt.plot([1, 2, -6, 0, 4])
# x = np.array([4, 5, 6, 7, 8])
# y = np.arange(0, 5, 1)
# x = np.array([a*a for a in y])
#
# y1 = [0, 1, 2, 3]
# x1 = [i+1 for i in y1]

# plt.plot(x, y, x1, y1)
# plt.plot(x, y, x1, y1, '--')
# plt.plot(x, y, x1, y1, ':')
# lines = plt.plot(x, y, x1, y1)
# plt.setp(lines, linestyle='-.')
# plt.plot(x1, y1)
# plt.plot(x, y)
# lines = plt.plot(x, y, '--r', x1, y1, '--g')
# lines = plt.plot(x, y, '--r', x1, y1, '--g', color='b')
# lines = plt.plot(x, y, '--r', x1, y1, '--g', color='#0000CC')
# lines = plt.plot(x, y, '--r', x1, y1, '--g', color=(0, 0, 0))
# lines = plt.plot(x, y, '--r', x1, y1, '--g', color=(0, 0, 0, 0.2))
# lines = plt.plot(x, y, '--ro', x1, y1, '--go', color=(0, 0, 0, 0.2))
# lines = plt.plot(x, y, '--r', x1, y1, '--g', marker='*', markerfacecolor='w')
# plt.setp(lines[0], linestyle='-.', marker='s', markerfacecolor='b', linewidth=4)

# filling graph areas

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
# plt.fill_between(x, y)
# plt.fill_between(x, y, 0.5)
plt.fill_between(x, y, where=(y < 0), color='r', alpha=0.5)
plt.fill_between(x, y, where=(y > 0), color='g', alpha=0.5)

plt.grid()

plt.show()