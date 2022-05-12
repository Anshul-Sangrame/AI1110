#Python libraries for symbols
import sympy
from sympy import *

#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Rotation Matrix
def rot(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    return  np.array([[c,-s],[s,c]]) 


#part-1: Finds the value of x

#variables
x = symbols('x')
lamda = symbols('lamda')


mat = np.array([x-2,1]) - lamda*np.array([3 + 2*x,-2])
sol_lamda = solve(Eq(mat[1],0),lamda)

for i in range(0,2) :
    mat[i] = mat[i].subs(lamda,sol_lamda[0])

sol_x = solve(Eq(mat[0],0),x)

x = x.subs(x,sol_x[0])
x = float(x)

print("x is {}".format(x))


#part-2: Verifies the result by ploting vector


a = np.array([1.0,0.0],dtype="float16")
theta = np.pi/6
b = 4*(rot(theta)@a)

alpha = (x-2)*a + b
betaf = (3+2*x)*a - 2*b
origin = [0,0]



plt.xlim(-13,13) 
plt.ylim(-14,14) 

print(alpha[0])
print(alpha[1])

#ax.quiver(b[0],b[1], a[0],a[1], angles='xy', scale_units='xy', scale=1, color = 'b')
plt.quiver(origin[0],origin[1], a[0],a[1], angles='xy', scale_units='xy', scale=1, color = 'b',label="a")
plt.quiver(origin[0],origin[1], b[0],b[1], angles='xy', scale_units='xy', scale=1, color = 'g',label="b")
plt.quiver(origin[0],origin[1], alpha[0],alpha[1], angles='xy', scale_units='xy', scale=1, color = 'r',label="alpha")
plt.quiver(origin[0],origin[1], betaf[0],betaf[1], angles='xy', scale_units='xy', scale=1, color = 'y',label="beta")

plt.grid()
plt.legend()

plt.savefig('G:/My Drive/IIT H/Semester-2/Probability/H.W/Assignment-2/figure/fig.pdf')
plt.show()
