class Temp:
    def __init__(self):
        self.__f = -40
        self.__c = -40


    def setFahrenheit(self, f):
        self.__f = f
        self.__c = (f - 32) * 5/9
    def setCelsius(self, c):
        self.__c = c
        self.__f = c * 9/5 + 32

    def getFahrenheit(self):
        return round(self.__f,2)

    def getCelsius(self):
            return round(self.__c,2)

# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():

    for temp in range(0, 212, 40):
        t = Temp()
        t.setFahrenheit(temp)
        print(str(t.getFahrenheit()), "Fahrenheit equals", str(t.getCelsius()) , "Celsius")
    
    for temp in range(0, 100, 20):
        t = Temp()
        t.setCelsius(temp)
        print(str(t.getCelsius()), "Celsius equals", str(t.getFahrenheit()), "Fahrenheit")

# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()

