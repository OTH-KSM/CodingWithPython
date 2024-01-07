#!/usr/bin/env python3

print("Welcome to my calculator!")
print("You can use the following operations: +, -, *, /, %")

n1 = input("Enter Your first number : ")
n2 = input("Enter Your second number : ")

if n1 == "" or n2 == "" or not n1.isdigit() or not n2.isdigit():
    print("Invalid Numbers Input")
    exit ()

op = input("which opeartion you want to apply : ")

if op == "+":
    print("The result is : " + str(int(n1) + int(n2)))
elif op == "-":
    print("The result is : " + str(int(n1) - int(n2)))
elif op == "*":
    print("The result is : " + str(int(n1) * int(n2)))
elif op == "/":
    print("The result is : " + str(int(n1) / int(n2)))
elif op == "%":
    print("The result is : " + str(int(n1) % int(n2)))
elif op == "-":
    print("The result is : " + str(int(n1) - int(n2)))
else:
    print("Invalid opeartion")