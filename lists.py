#!/usr/bin/env python3


def list_operations():
    # A list can hold multiple types of Values strings, numbers, boolean values ...
    friends = ["LOL", "MAD", False, 2, "MEY", 33.33]

    # printing the from and index to another 
    print(friends[1:4])
    # when indexing with negative numbers we indexing from the back of the list
    print(friends[-1])
    print(friends[2])
    print(friends[3])
    print(friends[4])
    print(friends[5])
    print("*******************************************************\n\n")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("printing friend List")
    print(friends)
    print("*******************************************************")

    print("printing numbers List")
    print(numbers)
    print("*******************************************************")

    #1 extanding two lists
    numbers.extend(friends)
    print("extanding two lists")
    print(numbers)
    print("*******************************************************")

    #2 adding an item into a list
    numbers.append(True)
    print("adding an item into a list")
    print(numbers)
    print("*******************************************************")

    #3 inserting an item in a specific place inside the list
    print("inserting an item in a specific place inside the list")
    numbers.insert(1, "MEY")
    print(numbers)
    print("*******************************************************")

    #4 remove an item from list
    numbers.remove(2)
    print("remove an item from list")
    print(numbers)
    print("*******************************************************")

    #5 pop delete the last element of the list
    numbers.pop()
    print("pop delete the last element of the list")
    print(numbers)
    print("*******************************************************")

    #6 checking if an iterm is in the list
    print("checking if an iterm is in the list")
    print("the index is : " + str(numbers.index("MEY")))
    print("*******************************************************")

    #6 count how many time an item repeated in the list
    print("count how many time an item repeated in the list")
    print("the item MEY repeated " + str(numbers.count("MEY")) + " times")
    print("*******************************************************")

    #7 Sort a list ; sort works with just multiple type
    print("Sort a list ; sort works with just multiple type")
    numbers = [ 6, 1, 8, 2, 9, 4, 5, 7, 3]
    numbers.sort()
    print(numbers)
    print("*******************************************************")

    # copy reverse

    numbers2 = numbers.copy()
    print("copying numbers into numbers2 list")
    print(numbers2)

    print("reverse numbers2 list")
    numbers2.reverse()
    print(numbers2)
    print("*******************************************************")

    #* clear and remove all the list
    print("clear and remove all the list")
    numbers.clear()
    print(7)
    print(numbers)
    print("*******************************************************")



# **************************    2D List    ************************************

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)