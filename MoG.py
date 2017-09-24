import numpy as np
import matplotlib.pyplot as plt
import math
import random
from scipy.stats import norm

def norm_prob(val,m,s):
	exponent = (( float(val) - m )**2)/(2*(s**2))
	div = float(1)/(math.sqrt(2*math.pi*(s**2)))
	p = float(div)*math.exp(exponent)
	return p

print("Mixture of Gaussians -- EM Algorithm Test")
#Create data, sample from normals, roughly inline with pixel data
I = 100
a = np.random.normal(200,20,(I/2))
b = np.random.normal(100,30,(I/2))

x = []
x = list(a) + list(b)
x = list(x)

plt.hist(x)
#plt.show()

#Calculate mean and standard dev of the total dataset
mean = float(sum(x))/I
print("Mean:\t\t\t%f"%mean)

std = np.std(x)
print("Standard Deviation:\t%f\n\n"%std)

#Start EM algorithm for MoG!!!!
#Initialise theta (parameters) to random values for K Gaussians
K = 2
lambda_mog = [float(1)/K]*K
mu = []
sigma = []

for k in xrange(0,K):
	mu.append(random.choice(x))
	sigma.append(std)

#Begin main loop
count = 1
print norm_prob(x[3],150,50)

while(count < 10):
	print("Itteration %d:\n"%count)
	l = [[0 for y in xrange(K)] for x in xrange(I)]
	r = [[0 for y in xrange(K)] for x in xrange(I)]
	for i in xrange(0,I):
		for k in xrange(0,K):
			print(x[1])
			v =  norm_prob(float(x[i]),1,1)
	
	count = count + 1
