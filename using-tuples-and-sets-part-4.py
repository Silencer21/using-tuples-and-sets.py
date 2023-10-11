#import required modules
from pprint import pprint
from collections import namedtuple

#create named tuple to store info
Dev_info = namedtuple('Dev_info', ['name','os','ip','user','password'])

#create dictionary
devices = {}

#open file and read device info
file = open('devices-04.txt', 'r')
for line in file:
    #add device in named tuple
    device_info = Dev_info(*(line.strip().split(',')))
    #display what has been read
    print('Device Information: ', device_info)
    #add named tuple to dictionary
    devices[device_info.name] = device_info

#display blank line for better reading
print('')

#display title
print('Input converted to a dictionary of named tuples:')

#display tuple
pprint(devices)

#close file 
file.close()

