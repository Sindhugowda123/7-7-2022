#program for addition

#!/usr/bin/python3

def add(num1,num2):
    return num1+num2

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("Sum of {0} and {1} is {2}".format(num1,num2,add(num1,num2)))
