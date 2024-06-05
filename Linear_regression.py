import matplotlib.pyplot as plt
from scipy import stats

# sample data
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#scipy function
slope, intercept, r, p, std_err = stats.linregress(x, y)

def newValue(x):
  return slope * x + intercept

model = list(map(newValue, x))

# relationship between the x and y (0 = no relation)
print(r)

# sample data plotted
plt.scatter(x, y)
plt.show()

# linear regression
plt.scatter(x, y)
plt.plot(x, model)
plt.show()