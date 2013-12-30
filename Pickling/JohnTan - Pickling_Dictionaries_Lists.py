'''
Name: John Tan
MTH 4320
Date: 9/14/2013
'''

import pickle

#Create an empty list to hold the dictionaries
inventory = []


#Dictionaries of Mac(101), Ipod(102), Iphone(103), Ipad(104)
Mac = {101:[101,'MacBook Air',1099.00],
       102:[102,'MacBook Pro',1299.00]}

Ipod = {103:[103,'Ipod Shuffle',49.00],
        104:[104,'Ipod Nano',149.00],
        105:[105,'Ipod Touch',229.00],
        106:[106,'Ipod Classic',249.00]}

Iphone = {107:[107,'Iphone 5S',199.00],
          108:[108,'Iphone 5C',99.00],
          109:[109,'Iphone 4S',49.00]}

Ipad = {110:[110,'Ipad Mini',329.00],
        111:[111,'Ipad 2',399.00]}

inventory.append(Mac)
inventory.append(Ipod)
inventory.append(Iphone)
inventory.append(Ipad)

#open file to write in binary 
datapickle = open('data.p','wb')

#pickle it/dump data into the file
pickle.dump(inventory,datapickle)

#close file
datapickle.close()


