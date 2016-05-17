from sympy import *

x = Symbol('x')
y = Symbol('y')
f = Function('f')

def limite(func, tende, x=x):
    print(limit(func, x, tende))

def derivada():
    pass


limite(x**2 - 5*x + 3, 4)
