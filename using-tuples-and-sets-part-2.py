#import required modules
from pprint import pprint

#open file and read in single line
file = open('devices-05.txt','r')
file_line = file.readline().strip()

#display line read
print('Read line: ', file_line)

#convert to a tuple using split()
device_info = tuple(file_line.split(','))

#display blank line
print('')

#display title
print('Input converted to a tuple:')

#display dictionary
pprint(device_info)

#close the file
file.close
