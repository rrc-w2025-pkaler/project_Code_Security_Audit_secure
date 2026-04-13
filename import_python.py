"""
Description: Introduction to Import Statements and File I/O
Author: Parneet kaler
Date: February 2025
Usage: To execute, press the play button in the VSC IDE.
"""
# IMPORT STATEMENTS
import math
import random 
from pprint import pprint 

# Variables used in this demonstration
radius = 12.5
square = 144
fruits = ["apple", "banana", "cherry"]

# USING IMPORTED MODULES


# RANDOM
print(random.random())
print(random.randint(1, 10))
print()
print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)

print()
# FILE I/O
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

#Writing to a file
file = open("output.txt", "w")
file.write("Hello World!")
file.close()



print()

# WITH CLAUSE
with open("example.txt", "r") as file:
    content = file.read()
    print(content)



# READ INTO DICTIONARY
data = {}
with open("dict_example.txt", "r") as input_file:
    for line in input_file:
        key, value = line.strip().split('*')
        data[key] = int(value)
print(data)
print()
pprint(data)