try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (not 0): "))
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    fraction = numerator / denominator
    print(fraction)
except ValueError as ve:
    print(ve)
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
