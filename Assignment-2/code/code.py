import sympy
from sympy import *
import numpy as np

#variables
x = symbols('x')
lamda = symbols('lamda')


mat = np.array([x-2,1]) - lamda*np.array([3 + 2*x,-2])
sol_lamda = solve(Eq(mat[1],0),lamda)

for i in range(0,2) :
    mat[i] = mat[i].subs(lamda,sol_lamda[0])

sol_x = solve(Eq(mat[0],0),x)

print("x is",sol_x[0])
