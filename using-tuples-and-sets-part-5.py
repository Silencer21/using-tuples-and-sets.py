#import modules
from pprint import pprint
from collections import namedtuple

#create named tuple
Dev_info = namedtuple('Dev_info', ['name','os_type','ip','user','password'])

#create a set for holding OS types
os_types = set()

#open file and read in the device info
file = open('devices-04.txt','r')
for line in file:
    #add device info into named tuple
    device_info = Dev_info(*(line.strip().split(',')))
    #display what read
    print('Device Information: ',device_info)
    #add the OS type to set
    if device_info.os_type not in os_types:
        os_types.add(device_info.os_type)

#display blank line
print('')

#display title
print('Input converted to a set of OS types present:')

#display the tuple
pprint(os_types)

#close file
file.close()
