'''
Name: John Tan
Date: 8/31/2013
'''

#HW.1 - define a volume of rectangle and area of square

from math import *

def rectangle(l, w, h):
    volume = (l * w * h)
    return volume 

def square(l, w):
    area = l * w
    return area

print ("Please choose the shape you want to calculate")
print ("Rectangle = 1")
print ("square = 2")
print ("--------------------------------")

user_input = 0
while user_input not in (1,2):
    user_input = int(input("Enter your Choice:"))

    if user_input not in (1,2):
        print("INVALID ENTRY!")

#Rectangle---------------------------------------------------
if (user_input == 1):
    print("Area of Rectangle:")
    length = int(input("Enter the length of Rectangle: "))
    width = int(input("Enter the width of Rectangle: "))
    height = int(input("Enter the height of Rectangle: "))
    volume = rectangle(length,width,height)
    print("The Volume of Rectangle is: ",volume)
#-----------------------------------------------------------


#Square------------------------------------------------------
elif (user_input == 2):
    print("Area of Square: ")
    length = int(input("Enter the length of Square: "))
    width = int(input("Enter the width of Square: "))
    area = square(length,width)
    print("The Area of Square is: ",area)
#------------------------------------------------------------



