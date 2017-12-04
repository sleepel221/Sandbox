"""
Wee Jian Jie Marcus
"""

name = input("Enter your name: ")

while name == "":
    name = input("Enter your name: ")

print(name[1::2])