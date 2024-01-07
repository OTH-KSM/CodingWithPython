#!/usr/bin/env python3

# The tuples are like lists but the difference is that you can't change values inside a tuple
# and you can't add or delete data from it we can say that a tuple is a constant list that made
# to hold data that will not modified


coordinate = (5, 3)
coordinate1 = (3, 2)
# coordinate[1] = 10
#  'tuple' object does not support item assignment

print(coordinate.index(3))
print(len(coordinate))

# we can create a list of tuples 

list_of_tuples = [(3, 2), coordinate, (5, 5), coordinate1]
print(list_of_tuples)

list_of_tuples[0] = (0, 0)
print(list_of_tuples)