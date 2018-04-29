import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
low = np.inf
high = -np.inf

# find the overall min/max
chunksize = 1000
loop = 0
for chunk in pd.read_table('dataforfit1.txt', header=None, chunksize=chunksize, delimiter='\t'):
    low = np.minimum(chunk.iloc[0].min(), low)
    high = np.maximum(chunk.iloc[0].max(), high)
    loop += 1
lines = loop*chunksize

nbins = math.ceil(math.sqrt(lines))   

bin_edges = np.linspace(low, high, nbins + 1)
total = np.zeros(nbins, np.int64)  # np.ndarray filled with np.uint32 zeros, CHANGED TO int64


# iterate over your dataset in chunks of 1000 lines (increase or decrease this
# according to how much you can hold in memory)
for chunk in pd.read_table('dataforfit1.txt', header=None, chunksize=2, delimiter='\t'):

    # compute bin counts over the 3rd column
    subtotal, e = np.histogram(chunk.iloc[0], bins=bin_edges)  # np.ndarray filled with np.int64

    # accumulate bin counts over chunks
    total += subtotal


plt.hist(bin_edges[:-1], bins=bin_edges, weights=total)
plt.bar(np.arange(total.shape[0]), total, width=1)
plt.savefig('gsl_test_hist.svg')
