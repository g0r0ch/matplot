import numpy as np
import matplotlib.pyplot as plt



fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-10*np.pi, 10*np.pi, 0.5)
# ax.plot(x, np.sinc(x) * np.exp(- np.abs(x/10)))
#log scale

# ax.semilogy(x, np.sinc(x) * np.exp(- np.abs(x/10)))
# ax.semilogx(x, np.sinc(x) * np.exp(- np.abs(x/10)))

ax.plot(x, np.sinc(x) * np.exp(- np.abs(x/10)))
# ax.set_yscale('log', base=5, subs=[2, 9])
ax.set_xscale('symlog', linthresh=2)

ax.grid()
plt.show()