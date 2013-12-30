'''
Name: John Tan
Date: 9/19/2013
'''


from math import *

'''
Complex Number: a + bi
a = real number
bi = imaginary number
'''

class ComplexNum(object):
    #initialize a and b
    def __init__(self,a,b):
        self.a = a  
        self.b = b 

    #declare string functio nand apply string class to a and b
    def __str__(self):
        if type(self.a) == int and type(self.b) == int: #if it's type integer
            if self.b >= 0:  #if the real number is >= 0, returns the string of a and b 
                return '%a+%ai'%(self.a,self.b)
            elif self.b < 0: #if the real number is < 0, returns the string of a and b
                return '%a+%ai'%(self.a,self.b)
            else:
                if self.b <= 0: #if real number is <= 0, returns the string of a and b
                    return '%b+%bi'%(self.a,self.b)
                elif self.b > 0: #if real number is > 0, returns the string of a and b
                    return '%b+%bi'%(self.a,self.b)
                
    #ADDITION
    def __add__(self,other):
        r1 = self.a
        i1 = self.b
        r2 = other.a
        i2 = other.b
        #ie: (r1+i1)(r2+i2) 
        #ex: (2+3i)(1+4i) = 3+7i
        R = r1 + r2
        I = i1 + i2
        result = ComplexNum(R,I)
        return result

    #SUBTRACTION
    def __sub__(self,other):
        r1 = self.a
        i1 = self.b
        r2 = other.a
        i2 = other.b
        #ie: (r1+i1)(r2+i2) = (r1-r2),(i1-i2)
        #ex: (2+3i)(1+4i) = 2-1+4i-3i = 1+-1i
        R = r1 - r2
        I = i1 - i2
        result = ComplexNum(R,I)
        return result

    #MULTIPLICATION
    def __mul__(self,other):
        r1 = self.a
        i1 = self.b
        r2 = other.a
        i2 = other.b
        #ie: (r1+i1)(r2+i2) = (r1*r2-i1*i2),(i1*r2+r1*i2)
        #ex: (2+3i)(1+4i) = 2*1-3i*4i+3i*1+2*4i = -10+11i
        R = (r1*r2-i1*i2)
        I = (i1*r2+r1*i2)
        result = ComplexNum(R,I)
        return result

    #INTEGER DIVISION
    def __floordiv__(self,other):
        r1 = self.a
        i1 = self.b
        r2 = other.a
        i2 = other.b
        #ex:(a+bi)/(c+di) = (a+bi)(c-di)/(c+di)(c-di)
        R = int(r1*r2+i1*i2)//int(r2*r2+i2*i2)
        I = int(i1*r2-r1*i2)//int(r2*r2+i2*i2)
        result = ComplexNum(R,I)
        return result

a = int(input("Enter the 1st real(R) number: "))
b = int(input("Enter the 1st imaginary(I) number: "))
c = int(input("Enter the 2nd real(R) number: "))
d = int(input("Enter the 2nd imaginary(I) number: "))

print("-----------------------------------------------------------")

ComplexNum1 = ComplexNum(a,b)
ComplexNum2 = ComplexNum(c,d)

print ("The 1st Complex Number is: ",ComplexNum1)
print ("The 2nd Complex Number is: ",ComplexNum2)
print ("-----------------------------------------------------------")

print (ComplexNum1,"+",ComplexNum2,"=",ComplexNum1+ComplexNum2)
print (ComplexNum1,"-",ComplexNum2,"=",ComplexNum1-ComplexNum2)
print (ComplexNum1,"x",ComplexNum2,"=",ComplexNum1*ComplexNum2)
print (ComplexNum1,"/",ComplexNum2,"=",ComplexNum1//ComplexNum2)
