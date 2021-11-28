#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
#start
cost_of_gallon = float(input("Enter cost per gallon:\t\t"))
#end

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 1)
#Start
#calculate total gas cost
total_cost = gallons_used * cost_of_gallon
total_cost = round(total_cost, 1)
#calculate cost per mile
cost_of_mile = cost_of_gallon / mpg
cost_of_mile = round(cost_of_mile, 1)
#end
            
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
#start
print(f"Total Gas Cost:\t\t\t{total_cost}")
print(f"Cost Per Mile:\t\t\t{cost_of_mile}")
#end
print()
print("Bye!")


