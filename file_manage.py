#!/usr/bin/env python3
'''
Openning file with Modes
r = read
w = write
a = append
r+ = read and write
'''

# ****************** Reading From File *********************

fd = open("file.txt", "r")

# check if the file is readable True or False
print(fd.readable())

# read from file line by line
for i in fd.readlines():
    print(i)

fd.close()

# ****************** Writing Into File *********************

fd1 = open("file1.txt", "a")

# check if the file is writable True of false
print(fd1.writable())

fd1.write("howwwwwww")

fd1.close()