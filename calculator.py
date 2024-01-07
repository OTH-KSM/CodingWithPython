#!/usr/bin/env python3
import fun

print("Welcome to my calculator!")
print("You can use the following operations: +, -, *, /, %")

n1 = input("Enter Your first number : ")
n2 = input("Enter Your second number : ")

if n1 == "" or n2 == "" or not n1.isdigit() or not n2.isdigit():
    print("Invalid Numbers Input")
    exit ()

op = input("which opeartion you want to apply : ")

if op == "+":
    print("The result is : " + fun.sum(n1, n2))
elif op == "-":
    print("The result is : " + fun.sub(n1, n2))
elif op == "*":
    print("The result is : " + fun.mul(n1, n2))
elif op == "/":
    print("The result is : " + fun.div(n1, n2))
elif op == "%":
    print("The result is : " + fun.mod(n1, n2))
else:
    print("Invalid opeartion")