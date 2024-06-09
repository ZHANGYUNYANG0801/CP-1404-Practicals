is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set is_finished to True to exit the loop if an integer is entered
    except ValueError:  # Catch the specific exception for invalid input
        print("Please enter a valid integer.")

print("Valid result is:", result)
