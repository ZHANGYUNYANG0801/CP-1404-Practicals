# Part to display all the odd numbers between 1 and 20 with a space between each one
print("Odd numbers between 1 and 20:")
for i in range(1, 21, 2):
    print(i, end=' ')
print()  # Newline for separation

# a. Count in 10s from 0 to 100
print("Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()  # Newline for separation

# b. Count down from 20 to 1
print("Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()  # Newline for separation

# c. Print n stars. Ask the user for a number, then print that many *, all on one line.
n = int(input("Enter the number of stars: "))
print("Stars:")
for i in range(n):
    print('*', end='')
print()  # Newline for separation

# d. Print n lines of increasing stars.
print("Increasing stars:")
for i in range(1, n + 1):
    print('*' * i)
