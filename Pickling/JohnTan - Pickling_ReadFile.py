'''
Name: John Tan
MTH 4320
Date: 9/14/2013
'''

import pickle

#open the file to read
infile = open('data.p','rb')

#load the file into data
data = pickle.load(infile)

'''
User can Add items to a shopping cart and the number of quantities for each items.
Once you are done shopping, it will give you a grand total of all the items
that you have shopped.
'''

print('--------------------------------------------------------')

#assign each index for each dictionary
Mac = data[0]
Ipod = data[1]
Iphone = data[2]
Ipad = data[3]

#this will print the dictionary name and ouput the keys that will display the values for each key
print('MAC: ')
for key in Mac.keys():
    print (Mac[key])

print('--------------------------------------------------------')

print('IPOD: ')
for key in Ipod.keys():
    print (Ipod[key])

print('--------------------------------------------------------')

print('IPHONE: ')
for key in Iphone.keys():
    print (Iphone[key])

print('--------------------------------------------------------')

print('IPAD: ')
for key in Ipad.keys():
    print (Ipad[key])

print('--------------------------------------------------------')
print('ENTER THE PRODUCT KEY FOR ORDERS')

print('[Key] = [Product Name]',
    '\n101 = MacBook Air',
    '\n102 = MacBook Pro',
    '\n103 = Ipod Shuffle',
    '\n104 = Ipod Nano',
    '\n105 = Ipod Touch',
    '\n106 = Ipod Classic',
    '\n107 = Iphone 5S',
    '\n108 = Iphone 5C',
    '\n109 = Iphone 4S',
    '\n110 = Ipad Mini',
    '\n111 = Ipad 2')

print('--------------------------------------------------------')

#grand total starts with 0 value and it will add up throughout the while loop 
grandtotal = 0

while True:
    item = int(input("ADD THE ITEMS YOU WISH TO ORDER\n(ENTER '1' ONCE YOU ARE DONE WITH YOUR ORDERS)\n>>"))

    #set a condition for each item number
    #allow user to set the price
    #allow user input the number of quantity
    #output the total for each item and multiply it with the number of quantity
    #set grandtotal under each condition of items so it could obtain the grandtotal of the user's total purchase
    if item == 101:
        print(Mac[item])
        price = Mac[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price*quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    elif item == 102:
        print(Mac[item])
        price = Mac[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price * quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    elif item == 103:
        print(Ipod[item])
        price = Ipod[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price * quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    elif item == 104:
        print(Ipod[item])
        price = Ipod[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price * quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    elif item == 105:
        print(Ipod[item])
        price = Ipod[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price * quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    elif item == 106:
        print(Ipod[item])
        price = Ipod[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price * quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    elif item == 107:
        print(Iphone[item])
        price = Iphone[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price * quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    elif item == 108:
        print(Iphone[item])
        price = Iphone[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price * quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    elif item == 109:
        print(Iphone[item])
        price = Iphone[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price * quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    elif item == 110:
        print(Ipad[item])
        price = Ipad[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price * quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    elif item == 111:
        print(Ipad[item])
        price = Ipad[item][2]
        quantity = int(input("ENTER NUMBER OF QTY: "))
        total = (price * quantity)
        grandtotal += (price * quantity)
        print("Total:","$%0.2f "%(total))
        print('--------------------------------------------------------')

    else:
        print("You have exited the shopping cart.\nThank You!")
    
    if item == 1:
        break

print('--------------------------------------------------------')

#output the grand total with 2 decimal places 
print("Grand Total:","$%0.2f " %(grandtotal))









    


