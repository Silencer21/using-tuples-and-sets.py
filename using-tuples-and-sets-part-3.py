#import modules
from pprint import pprint

#create outer list for all devices
devices = []

#open file and read in device info
file = open('devices-04.txt','r')
for line in file:
    #add device info to tuple
    device_info = tuple(line.strip().split(','))
    #display what read
    print('Read line: ', device_info)
    #append device and info into devices list
    devices.append(device_info)

#display blank line
print('')

#display title
print('Input converted to a list tuples:')

#display tuple 
pprint(devices)

#close the file
file.close()

