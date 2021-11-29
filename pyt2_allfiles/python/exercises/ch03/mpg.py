#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")


cont = True

while cont:
    print()
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_gallons = float(input("Enter cost per gallon:      "))

    while miles_driven <= 0:
        print()
        miles_driven = float(input("Miles driven must be greater than zero. Please try again: "))
    while gallons_used <= 0:
        print()
        gallons_used = float(input("Gallons used must be greater than zero. Please try again: "))
    while gallons_used <= 0:
        print()
        cost_gallons = float(input("Cost per gallon used must be greater than zero. Please try again: "))

    # calculate and display miles per gallon
    print()
    mpg = round(miles_driven / gallons_used, 2)
    print("Miles Per Gallon:          ", mpg)
    total_cost = round(gallons_used * cost_gallons, 2)
    print("Total Gas Cost:            ", total_cost)
    cost_mile = round(cost_gallons / mpg, 2)
    print("Cost Per Mile:             ", cost_mile)

    answer = str(input("Get entries for another trip (y/n)? "))
    while answer != "y" and answer != "n":
        print()
        print("Invalid Selection! Chose again")
        answer = str(input("Get entries for another trip (y/n)? "))
    if answer == "n":
        cont = False




