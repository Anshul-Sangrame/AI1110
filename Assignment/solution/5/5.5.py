#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy

nv = np.loadtxt('gau.dat', dtype='double')
bv = np.loadtxt('ber.dat', dtype='double')
sig = np.loadtxt('ber_gau.dat',dtype='double')
e0 = np.count_nonzero((sig < 0) & (bv > 0))
n0 = np.count_nonzero(bv > 0)
e1 = np.count_nonzero((sig > 0) & (bv < 0))
n1 = np.count_nonzero(bv < 0)
print("X = 1: ", e0/n0)
print("X = -1: ", e1/n1)