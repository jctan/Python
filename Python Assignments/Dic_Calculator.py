'''
Name: John Tan
Date: 8/31/2013
'''

#HW.2 - create a calculator using dictionary to look up the operations 

from math import *

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 + n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 * n2

def power(n1,n2):
    return n1 ** n2

opers = {'+':add,
         '-':sub,
         '*':mult,
         '/':div,
         '^':power}

print('+ ',
      '- ',
      '* ',
      '/ ',
      '^ ')
print('This is a ###CALCULATOR###')
print('Please calculate using any of these operators.')

while True:
    expr = input('> ')
    if expr:
        try:
            (op1, op, op2) = expr.split(' ')
            print(opers[op](int(op1),int(op2)))
        except Exception:
            print("Sorry, I couldn't make sense of that")
    else:
        break
