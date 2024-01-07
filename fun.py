#!/usr/bin/env python3


# *****************************************************
# funciton syntax
# def say_hi(name, age):
#     print("Hello " + name + "! you are " + str(age))

# print("Top")
# say_hi("Othmane", 70)
# print("Bottom")

# # return value
# def cub_num(nbr):
#     return pow(nbr, 3)

# result = cub_num(3)
# print(result)
# *****************************************************


# function to be used by the calculator

def sum(nbr1, nbr2):
    return str(int(nbr1) + int(nbr2))

def sub(nbr1, nbr2):
    return str(int(nbr1) - int(nbr2))

def mul(nbr1, nbr2):
    return str(int(nbr1) * int(nbr2))

def div(nbr1, nbr2):
    return str(int(nbr1) / int(nbr2))

def mod(nbr1, nbr2):
    return str(int(nbr1) % int(nbr2))

