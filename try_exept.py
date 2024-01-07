#!/usr/bin/env python3

'''
num = 10/0
it should be inside try
Anything outside try will not catched
'''
# type-casting the input directely into integer
try:
    # num = 10/0
    number = int(input("Enter a number : "))
    print(number)

except ZeroDivisionError:
    print("Divition by zero")
except ValueError as err: # saving the error inside err
    print(err) 


'''
list of error to be catched
ModuleNotFoundError
MemoryError
do except followed by E : to see all errors to be catched
'''


