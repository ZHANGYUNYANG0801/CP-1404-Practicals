import random

# Constants
STARTING_PRICE = 10.00
MIN_PRICE = 1.00
MAX_PRICE = 100.00
MAX_INCREASE = 0.175  # 17.5%

# File to write output
FILENAME = "stock_prices.txt"

# Open file for writing
out_file = open(FILENAME, 'w')

# Initialize variables
price = STARTING_PRICE
day = 0

# Simulate stock price changes
while MIN_PRICE <= price <= MAX_PRICE:
    # Increment day
    day += 1

    # Calculate price change
    price_change = 0
    if random.randint(1, 2) == 1:  # 50% chance of increase
        price_change = random.uniform(0, MAX_INCREASE)
    else:  # 50% chance of decrease
        price_change = -random.uniform(0, 0.05)  # 0 to 5%

    # Update price
    price += price * price_change

    # Output to file
    print(f"On day {day} price is: ${price:.2f}", file=out_file)

# Close the file
out_file.close()
