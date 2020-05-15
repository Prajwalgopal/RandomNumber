import matplotlib.pyplot as plt
import numpy as np

p = .4
n_bins=50
x = np.random.logseries(p, 100)
x.sort()
print(x)


y = -p**x/(x*np.log(1-p))
# y = y.cumsum()
# y /= y[-1]
print(y)
plt.plot(x, y, linewidth=2, color='r')
plt.title("Lgarithmic Distribution -> Probability Mass Function")
plt.xlabel('random numbers (x)')
plt.ylabel('P(x)')

fig1, ax1 = plt.subplots()
ax1.set_title('Lognormal Distribution >> PDF >> Histogram')
ax1.set_xlabel('random numbers (x)')
ax1.set_ylabel('P(x)')
ax1.grid(True)
n, bins, patches = ax1.hist(x, density=True, histtype='step',
                            label='Empirical')


fig2, ax2 = plt.subplots()
ax2.set_title('Box Plot')
ax2.boxplot(y)

plt.show()