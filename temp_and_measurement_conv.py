#   Name: Zachary Morrell
#   Date: September 4, 2023
#   Assignment name: Module 2 Exerciise - The IPO Pattern
#   Class Number: CIT 232 - Intro to Programming Logic
#
#   Compiled together programs with an option select method.

# Method to choose which type of conversion to use.
def option_select():
    program_menu = [
        "* This program allows a user to convert:        *",
        "* Option   -       Description                  *",
        "*===============================================*",
        "*    0          Close the program               *",
        "*    1        Celsius to Fahrenheit             *",
        "*    2        Fahrenheit to Celsius             *",
        "*    3        Inches to Centimeters             *",
        "*    4        Centimeters to Inches             *",
        "*===============================================*",
        "*   Type the preferred option and hit <ENTER>   *"]
    
    star_border = len(program_menu[0]) * "*"
    print(star_border)
    for line in program_menu:
        print(line)    
    print(star_border)

    valid_option = False
    while(valid_option == False):
        try:
            option = int(input("What would you like to do?: "))
            match(option):
                case 0:
                    exit()
                case 1:
                    valid_option = True
                    celsius_to_fahrenheit()
                case 2:
                    valid_option = True
                    fahrenheit_to_celsius()
                case 3:
                    valid_option = True
                    inches_to_centimeters()
                case 4:
                    valid_option = True
                    centimeters_to_inches()
                case _:
                    print(option,"is not a valid option.")
        except ValueError:
            print("The input must be a number, refer to the instructions above.")

# Continue program or return to menu method.
def continue_calc(current_program):
    programs = [option_select, celsius_to_fahrenheit, fahrenheit_to_celsius, inches_to_centimeters, centimeters_to_inches]
    option = input("\nWould you like to continue with this program? (y/n): ").lower()
    if(option == "y" or option == "yes"):
        programs[current_program]()
    else:
        programs[0]()

# Option 1 - Method to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit():
    print("\nThis program converts the temperature in Celsius to the equivalent in Fahrenheit.")
    degreesInCelsius = float(input("Enter a Celsius Temperature: "))
    degreeInFahrenheit = degreesInCelsius * 9/5 + 32
    print("The result is:",degreeInFahrenheit, " degrees Fahrenheit.")
    continue_calc(1)

# Option 2 - Methond to convert Fahrenheit to Celsius.
def fahrenheit_to_celsius():
    print("\nThis program converts the temperature in fanhrenheit to the equivalent in celsius.")
    degrees_in_fahrenheit = float(input("Enter the degrees in fahrenheit: "))
    degrees_in_celsius = (degrees_in_fahrenheit - 32) * (5/9)
    print("The result is:",degrees_in_celsius," degrees Celsius.")
    continue_calc(2)

# Option 3 - Method to convert inches to centimeters.
def inches_to_centimeters():
    print("\nThis program converts a given measurement in Inches to the equivalent measurement in Centimeters.")
    lengthInInches = float(input("Enter the length in Inches to convert to Centimeters: "))
    lengthInCentimeters = lengthInInches * 2.54
    print(lengthInInches, " Inches is equal to ",lengthInCentimeters," Centimeters")
    continue_calc(3)

# Option 4 - Method to convert Centimeters to Inches.
def centimeters_to_inches():
    print("\nThis program is to convert a given centimeters to inches.")
    length_in_centimeters = float(input("Enter the length in centimeters: "))
    length_in_inches = round(length_in_centimeters * 0.393701, 2)
    print(length_in_inches)
    continue_calc(4)

option_select()