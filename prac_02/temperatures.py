def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    # Get user input
    temp = float(input("Enter the temperature: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

    # Conversion
    if unit == 'C':
        converted_temp = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

