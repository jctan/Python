'''
Name: John Tan
Date: 9/19/2013
'''

# A dictionary with numbers that's represented in different bases (because hexademical value starts with A after 9)
num_rep = {10:'A',
           11:'B',
           12:'C',
           13:'D',
           14:'E',
           15:'F',
           16:'G',
           17:'H',
           18:'I',
           19:'J',
           20:'K',
           21:'L',
           22:'M',
           23:'N',
           24:'O',
           25:'P',
           26:'Q',
           27:'R',
           28:'S',
           29:'T',
           30:'U',
           31:'V',
           32:'W',
           33:'X',
           34:'Y',
           35:'Z'}

#A funtion that converts the base
def convertedBase(num,base):

    #raise an error that the user have to input the base between 2 and 35
    if not 1 < base < 36:
        raise ValueError('Base must be between 2-%d' % len(num_rep[remainder]))
    
    #Convert a number from a base to another base
    digits = ''
    while num > 0:
        remainder = num % base
        if 36 > remainder > 9:
            #the remainder that's in the dictionary, store them as string
            r_string = num_rep[remainder]
        else:
            #else still store the remainder as string
            r_string = str(remainder)
        digits = r_string + digits
        num = num // base
    return digits


num = int(input("Enter a number: "))
base = int(input("Enter the base that your number is in: "))


#Store the digits in numeral system as "digits"
digits = convertedBase(num,base)
print ("The digits in numeral system for the current base is called: ", digits)

print("--------------------------------------------------------")

#Enter the base the user would like to convert it to
convert = int(input("Enter the base you would like to convert to: "))

'''''Computer the converted digits by the converted base'''''

#Store the converted digits in numeral system as "converted_digits" from the converted base
converted_digits = convertedBase(num,convert)

#Output the converted digits in numeral system from the converted base 
print("The digits for the converted base is: ", converted_digits)

print("--------------------------------------------------------")
