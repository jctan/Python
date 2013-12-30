'''
Name: John Tan
Date: 9/19/2013
'''

#A recursive function that raises the fraction to a power

from math import *
from fractions import *

def power(base,exp):
    if exp == 0:
        return 1
    elif exp < 0: #if the power is negative, then it's 1/(base)^(-exp)
        return 1 / power(base,-exp)
    elif exp == 1:
        return base
    elif exp % 2 == 0:
        half = power(base,exp//2) #if power is even, divide it by 2 
        return half * half # return to half 2 times 
    else:
        return base * power(base,exp - 1) #it goes exponentially until it hits 1
                                          #i.e, base * base * base * 1




a = Fraction(4,5)
b = Fraction(1,2)
c = Fraction(5,7)
d = Fraction(2,3)
e = Fraction(3,4)

data = [a,b,c,d,e] #store the fractions into the data list

for i in range(0,len(data)):
    print(data[i])
    
print("\nThe fractions in sorted order: ")

for i in range(0,len(data)):
    data.sort() #sort the fractions that is stored in the list 
    print(data[i])

print("------------------------------------")

exp = int(input("\nEnter the exponent value as an integer: "))

result_list = [] #create a list for the fractions raised to a power

for i in range(0,len(data)):
    result = power(data[i],exp) #calcualte the power of each fractions
    result_list.append(result) #append the calculated fractions raised to power

result_list.sort() #sorts the result_list in order

for i in range(0,len(result_list)): #loop the result_list to display results
    print (result_list[i])
