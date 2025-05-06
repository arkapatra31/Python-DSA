import os

num1 = 10
num2 = num1
print("Address of num1:", id(num1))
print("Address of num2:", id(num2))
print("Value of num1:", num1)
print("Value of num2:", num2)

# Change the value of num2
num2 = 20
print("Address of num1:", id(num1))
print("Address of num2:", id(num2))
print("Value of num1:", num1)
print("Value of num2:", num2)


# OUTPUT
"""
Address of num1: 4397050800
Address of num2: 4397050800
Value of num1: 10
Value of num2: 10
Address of num1: 4397050800
Address of num2: 4397051120
Value of num1: 10
Value of num2: 20
"""

# Clear console
os.system("clear")

dict1 = {"name": "John", "age": 30}
dict2 = dict1
print("Address of dict1:", id(dict1))
print("Address of dict2:", id(dict2))
print("Value of dict1:", dict1)
print("Value of dict2:", dict2)

# Change the value of dict2
dict2["age"] = 40
print("Address of dict1:", id(dict1))
print("Address of dict2:", id(dict2))
print("Value of dict1:", dict1)
print("Value of dict2:", dict2)

# OUTPUT
"""
Address of dict1: 4341587072
Address of dict2: 4341587072
Value of dict1: {'name': 'John', 'age': 30}
Value of dict2: {'name': 'John', 'age': 30}
Address of dict1: 4341587072
Address of dict2: 4341587072
Value of dict1: {'name': 'John', 'age': 40}
Value of dict2: {'name': 'John', 'age': 40}
"""

# Reason why dict1 and dict2 have the same address is because they point to the same memory location
# When we assign dict2 = dict1, we are not creating a new memory location for dict2, we are just pointing to the same memory location as dict1
# When we change the value of dict2, we are changing the value of dict1 as well because they point to the same memory location
# To create a new memory location for dict2, we need to use the copy() method
