import matplotlib.pyplot as plt
import scipy.special as sps
count, bins, ignored = plt.hist(s, 50, normed=True)
y = bins**(shape-1)*(np.exp(-bins/scale) / (sps.gamma(shape) * scale **shape))
plot.plot(bins,y,linewidth=2, color = 'r')
plt.show()
