#!/usr/bin/env python3

# Creating a Student class

class student:
    
    def __init__(self, name, subject, age):
        self.name = name
        self.subject = subject
        self.age = age
    
    def introduce(self):
        print("Hey my name is " + self.name + " i'm " + str(self.age) + " and i study now " + self.subject)

