def celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

def kilometers_to_miles(km):
    return km * 0.62137119

def miles_to_kilometers(miles):
    return miles / 0.62137119

def kilogram_to_pound(kg):
    return kg * 2.20462

def pound_to_kilogram(pound):
    return pound / 2.20462

def unit_converter():
    print("Welcome to the Unit Converter!")

    while True:
        print("\nConversion Options:")
        print("1. Temperature (Celsius to Fahrenheit or Fahrenheit to Celsius)")
        print("2. Distance (Kilometers to Miles or Miles to Kilometers)")
        print("3. Weight (Kilograms to Pounds or Pounds to Kilograms)")
        print("4. Exit")

        try:
            choice = int(input("Choose a conversion option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                temp_choice = input("Convert:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nChoose 1 or 2: ")
                if temp_choice == "1":
                    celsius = float(input("Enter temperature in Celsius: "))
                    print(celsius,"°C is equal to", celsius_to_fahrenheit(celsius), "°F")
                    break
                elif temp_choice == "2":
                    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                    print(fahrenheit,"°F is equal to", fahrenheit_to_celsius(fahrenheit), "°C")
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 2:
            try:
                dist_choice = input("Convert:\n1. Kilometers to Miles\n2. Miles to Kilometers\nChoose 1 or 2: ")
                if dist_choice == "1":
                    km = float(input("Enter distance in kilometers: "))
                    print(km, "km is equal to", kilometers_to_miles(km), "miles")
                    break
                elif dist_choice == "2":
                    miles = float(input("Enter distance in miles: "))
                    print(miles, "miles is equal to", miles_to_kilometers(miles), "km")
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 3:
            try:
                weight_choice = input("Convert:\n1. Kilograms to Pounds\n2. Pounds to Kilograms\nChoose 1 or 2: ")
                if weight_choice == "1":
                    kg = float(input("Enter weight in kilograms: "))
                    print(kg, "kg is equal to", kilogram_to_pound(kg), "pounds")
                    break
                elif weight_choice == "2":
                    pounds = float(input("Enter weight in pounds: "))
                    print(pounds, "pounds is equal to" ,pound_to_kilogram(pounds), "kg")
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 4:
            print("Thanks for using the Unit Converter. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid choice.")

unit_converter()
