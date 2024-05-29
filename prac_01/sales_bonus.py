"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Get the initial sales amount
sales = float(input("Enter sales: $"))

# Loop to repeatedly ask for sales and calculate the bonus until a negative number is entered
while sales >= 0:
    # Calculate the bonus based on the sales amount
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15

    # Print the calculated bonus
    print(f"Bonus: ${bonus:.2f}")

    # Get the next sales amount
    sales = float(input("Enter sales: $"))

# Indicate the end of the program
print("Program terminated.")
