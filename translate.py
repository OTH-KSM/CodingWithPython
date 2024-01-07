#!/usr/bin/env python3

'''
Note : In Python, strings are immutable, which means they cannot
be changed after they are created.
'''

def translate(str: str):
    vowels = "aeoiuAEOIU"
    new_str = ""
    for i in range(len(str)):
        if vowels.find(str[i]) != -1:  # if letter.lower() in "aeiou"
            new_str += 'g'
        else:
            new_str += str[i]
    return (new_str)

input = input("Enter a phrase: ")
ret = translate(input)
print(ret)

