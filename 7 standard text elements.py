import numpy as np
import matplotlib.pyplot as plt

# y = np.arange(0, 5, 1)
# x = np.array([a*a for a in y])
# y2 = [0, 2, 3, 4, 5, 7]
# x2 = [i+1 for i in y2]
# lines = plt.plot(x, y, x2, y2)
#
# plt.minorticks_on()
# plt.grid(which='major', color = '#444', linewidth = 1)
# plt.grid(which='minor', color = '#aaa', ls = ':')
# # plt.grid()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
plt.figtext(0.05, 0.6, 'Text window', fontsize=24, color='r')
fig.suptitle('Head window')
ax.set(facecolor='#AAFFAA')
ax.set_xlabel('Ox')
ax.set_ylabel('Oy')
ax.text(0.5, 0.1, 'text sample', bbox={'boxstyle':'darrow', 'facecolor': '#AAAAFF'})
ax.annotate('prescr', xy=(0.2, 0.4), xytext=(0.6, 0.7),
            arrowprops={'facecolor':'gray', 'shrink':0.1})


plt.show()