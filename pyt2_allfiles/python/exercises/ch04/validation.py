#!/usr/bin/env python3

def get_float(message, low, high):
    check = float(input(message))
    while check <= low or check > high:
        print(f"Entry must be greater than {low} and less than or equal to {high}")
        check = float(input(message))
    return check


def get_int(message, low, high):
    check = int(input(message))
    while check < low or check > high:
        print(f"Entry must be greater than {low} and less than or equal to {high}")
        check = int(input(message))
    return check


def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value


def main():
    choice = "y"
    while choice.lower() == "y":

        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
