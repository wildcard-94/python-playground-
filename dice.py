# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
print("This is a dice stimulator")
x = "y"

while x == "y":
    num = random.randint(1, 6)
    if num == 1:
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------")
    if num == 2:
        print("-----------")
        print("|         |")
        print("| 0     0 |")
        print("|         |")
        print("-----------")
    if num == 3:
        print("-----------")
        print("|    0    |")
        print("|    0    |")
        print("|    0    |")
        print("-----------")
    if num == 4:
        print("-----------")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("-----------")
    if num == 5:
        print("-----------")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("-----------")
    if num == 6:
        print("-----------")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print("-----------")
    x = input("press y to roll again")

