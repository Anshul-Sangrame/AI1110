
#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux

#import subprocess
#import shlex

#end if

simlen = int(1e6) #number of samples
x = np.linspace(0,1,simlen)#points on the x axis
#randvar = np.random.normal(0,1,simlen)
sig = np.loadtxt('ber_gau.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')

plt.plot(x.T,sig,".")#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$n \\times 10^6$')
plt.ylabel('$y(n)$')

#if using termux
plt.savefig('../figs/5_2.png')
#plt.savefig('./figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
