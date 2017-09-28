import numpy as np
import matplotlib.pyplot as plt
import math
import random
from scipy.stats import norm

print("Mixture of Gaussians -- EM Algorithm Test")
#Create data, sample from normals, roughly inline with pixel data
I = 100
a = np.random.normal(200,20,(I/2))
b = np.random.normal(100,30,(I/2))

val = []
val = list(a) + list(b)
val = list(val)

print(len(val))

plt.hist(val)
#plt.show()

#Calculate mean and standard dev of the total dataset
mean = float(sum(val))/I
print("Mean:\t\t\t%f"%mean)

std = np.std(val)
print("Standard Deviation:\t%f\n\n"%std)

#Start EM algorithm for MoG!!!!
#Initialise theta (parameters) to random values for K Gaussians
K = 2
lambda_mog = [float(1)/K]*K
mu = []
sigma = []

for k in xrange(0,K):
	mu.append(random.choice(val))
	sigma.append(std)

#Begin main loop
count = 1

while(count < 10):
	print("Itteration %d:\n"%count)
	l = [[0 for y in xrange(K)] for x in xrange(I)]
	r = [[0 for y in xrange(K)] for x in xrange(I)]
	for i in xrange(0,I):
		for k in xrange(0,K):
			norm.pdf(val[i],mu[k],sigma[k])
	count = count + 1
