#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
length = int(input("Please enter the length:\t"))
height = int(input("Please enter the height:\t"))

# calculate area
area = length * height
#calculate perimeter
perimeter = (2 * length) + (2 * height)
# format and display the result
print()
print(f"Area = {area}")
print(f"Perimeter = {perimeter}")
print()
print("Thanks for using this program!")


