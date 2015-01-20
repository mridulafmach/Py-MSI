
bins = np.arange(mass[0],mass[-1],0.1)

x_binned = np.digitize(mass[:,0], bins)
x_numpyArray = np.array(mass[:,0])
y_numpyArray = np.array(intens)

y_sum = np.array([
    y_numpyArray[x_binned == i].sum()
    if len(y_numpyArray[x_binned == i]) > 0
    else 0
    for i in range(1, len(bins))])

x_max = np.array([
    np.median(x_numpyArray[x_binned == i])
    if len(x_numpyArray[x_binned == i]) > 0
    else 0
    for i in range(1, len(bins))])


# binnedData is a list of tuples; tuple elements are bin's-low-limit, bin's-high-limit, y-mean value
binnedData = [(bins[i], bins[i + 1], y_sum[i]) for i in range(len(y_sum))]

y_sum = np.zeros(shape=(1,bins.size))
x_max = np.zeros(shape=(1,bins.size))

for i in range(1, len(bins)):
    if (len(x_numpyArray[x_binned == i]) > 0):
      y_sum[0,i] = y_numpyArray[x_binned == i].sum()
      y_maxi = y_numpyArray[x_binned == i].argmax(axis=0)
      x_max[0,i] = x_numpyArray[x_binned == i][y_maxi] 
    else: 
      0
