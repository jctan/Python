'''
Name: John Tan
Date: 8/31/2013
'''

#A dictionary of country codes and then sort them

def China(CN):
    return CN

def United_States(US):
    return US

def Canada(CA):
    return CA

def Germany(DE):
    return DE

codes = {'DE':'Germany',
         'CN':'China',
         'US':'United States',
         'CA':'Canada'}

for key in codes.keys():
    print(key, "=", codes[key])

print('--------------------------------------')

print('This is in a sorted order: ')

for key in sorted(codes):
    print(key, "=", codes[key])
    

    


    
