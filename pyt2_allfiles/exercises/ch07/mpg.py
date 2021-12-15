#!/usr/bin/env python3
import csv

FILENAME = "trips.csv"


def write_trips(trips):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)


def read_trips():
    trips = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            trips.append(row)
    return trips


def list_trips(trips):
    print(f"Distance \tGallons \tMPG")
    for trip in trips:
        print(f"{trip[0]} \t{trip[1]} \t{trip[2]}")


def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:
        print("Entry must be greater than zero. Please try again.\n")
    return miles_driven


def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used


def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()
    trips = read_trips()
    more = "y"
    while more.lower() == "y":
        list_trips(trips)
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round((miles_driven / gallons_used), 2)
        trips.append([miles_driven, gallons_used, mpg])

        more = input("More entries? (y or n): ")
    write_trips(trips)

    print("Bye!")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        
        more = input("More entries? (y or n): ")
    
    print("Bye!")

if __name__ == "__main__":
    main()