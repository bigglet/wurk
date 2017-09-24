import numpy as np
import matplotlib.pyplot as plt
import math

print("Mixture of Gaussians -- EM Algorithm Test")
#Create data, sample from normals, roughly inline with pixel data
I = 100
a = np.random.normal(200,20,(I/2))
b = np.random.normal(100,30,(I/2))

x = list(a) + list(b)

plt.hist(x)
plt.show()

#Calculate mean and standard dev of the total dataset
mean = float(sum(x))/I
print("Mean:\t\t%f"%mean)

std = np.std(x)
print("Standard Deviation:\t%f"%std)

