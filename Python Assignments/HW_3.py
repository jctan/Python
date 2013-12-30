'''
Name: John Tan
Date: 8/31/2013
'''

from math import *

#Example1: f(x)=x^3-2x-5
#          f'(x)=3x^2-2

#Example2: f(x)=x^6-2
#          f'(x)=6x^5


print('''
       Please input any X value to evaluate the following equaltion:
       Example 1: square(x)
       Example 2: cube(x)
       Example 3: f(x) = x^3-2x-5 //f(x)
       Example 4: f'(x) = 3x^2-2 //dfdx(x)
       Example 5: f(x) = x^6-2 //f1(x)
       Example 6: f'(x) = 6x^5 //dfdx1(x)
       ''')

def square(x):
    return x * x

def cube(x):
    return x * square(x)

def f(x):
    return cube(x) - 2 * x - 5

def dfdx(x):
    return 3 * square(x) - 2

def f1(x):
    return cube(x) * cube(x) - 2

def dfdx1(x):
    return 6 * cube(x) * sqaure(x)
