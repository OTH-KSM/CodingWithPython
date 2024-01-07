#!/usr/bin/env python3

month_conversions = {
    "Jan" : "January", # 1 : "January" -> we can use integers
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}


print(month_conversions[3])
# The use of get method in case the item is not in the dictionary it returns None to specify the the item doesn't exist
print(month_conversions.get("KOL"))

# We can change the message that appears when the item doesn't exist like this :
print(month_conversions.get("KOL", "Item doesn't exist"))
