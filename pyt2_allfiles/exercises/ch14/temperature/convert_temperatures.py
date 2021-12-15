import temperature as temp

def display_menu():
    print("The Convert Temperatures program")
    print()
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenhit")
    print()

def convert_temp():
    t = temp.Temp()
    option = int(input("Enter a menu option: "))
    if option == 1:
        t.setFahrenheit(int(input("Enter degrees Fahrenheit: ")))
        print("Degrees Celsius:", t.getCelsius())
    elif option == 2:
        t.setCelsius(int(input("Enter degrees Fahrenheit: ")))
        print("Degrees Fahrenheit:", t.getFahrenheit())
    else:
        print("You must enter a valid menu number.")

def main():
    display_menu()
    
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        
        again = input("Convert another temperature? (y/n): ")
        print()
        
    print("Bye!")

if __name__ == "__main__":
    main()
