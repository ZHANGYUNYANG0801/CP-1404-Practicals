# Get the number of items with input validation
num_items = int(input("Number of items: "))
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

total_price = 0

# Get the price of each item and compute the total price
for i in range(num_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply discount if total price is over $100
if total_price > 100:
    discount = total_price * 0.10
    total_price -= discount

# Display the total price with 2 decimal places
print(f"Total price for {num_items} items is ${total_price:.2f}")
