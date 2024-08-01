import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
# plt.subplot(1, 3, 1)
# plt.plot(np.random.random(10))
# plt.subplot(1, 3, 2)
# plt.plot(np.random.random(10))
# plt.subplot(1, 3, 3)
# plt.plot(np.random.random(10))
# plt.grid()

# ax = plt.subplot(1, 3, 1)
# plt.plot(np.random.random(10))
# ax1 = plt.subplot(1, 3, 2)
# plt.plot(np.random.random(10))
# ax2 = plt.subplot(1, 3, 3)
# plt.plot(np.random.random(10))
# ax.grid()
# # ax1.grid()
# ax2.grid()


# ax = plt.subplot(2, 3, 1)
# plt.plot(np.random.random(10))
# ax1 = plt.subplot(2, 3, 2)
# plt.plot(np.random.random(10))
# ax2 = plt.subplot(2, 3, 3)
# plt.plot(np.random.random(10))
# ax3 = plt.subplot(2, 1, 2)
# plt.plot(np.random.random(10))
# ax.grid()
# ax1.grid()
# ax2.grid()

# same as previous
# ax = plt.subplot(231)
# plt.plot(np.random.random(10))
# ax1 = plt.subplot(232)
# plt.plot(np.random.random(10))
# ax2 = plt.subplot(233)
# plt.plot(np.random.random(10))
# ax3 = plt.subplot(212)
# plt.plot(np.random.random(10))
# ax.grid()
# ax1.grid()
# ax2.grid()


# subplots

# f, ax = plt.subplots(2, 2)
# f.set_size_inches(7, 4) # size
# f.set_facecolor('#eee') # color
# ax[0, 0].plot(np.arange(0, 5, 0.2))
# ax[0, 0].grid()
# ax[0, 1].plot(np.arange(5, 0, -0.2))
# ax[0, 1].grid()

# new fig

# fig = plt.figure(figsize=(7, 4))
# ax1 = fig.add_subplot(1, 3, 1)
# ax1.plot(np.arange(5, 0, -0.2))
# # plt.plot(np.arange(0, 5, 0.2))
# f, ax = plt.subplots(2, 2)
# f.set_size_inches(7, 4) # size
# f.set_facecolor('#eee') # color
# ax[0, 0].plot(np.arange(0, 5, 0.2))
# ax[0, 0].grid()
# ax[0, 1].plot(np.arange(5, 0, -0.2))
# ax[0, 1].grid()

# GridSpec

ws = [1, 2, 5]
hs = [2, 0.5]

fig = plt.figure(figsize=(7, 4))
gs = GridSpec(ncols=3, nrows=2, figure=fig, width_ratios=ws, height_ratios=hs)
ax1 = plt.subplot(gs[0, 0])
ax1.plot(np.arange(0, 5, 0.2))

ax2 = fig.add_subplot(gs[1, 0:2])
ax2.plot(np.random.random(10))

ax3 = fig.add_subplot(gs[:, 2])
ax3.plot(np.random.random(10))

plt.show()