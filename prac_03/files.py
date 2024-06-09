# Write user's name to a file
name = input("Enter your name: ")
with open("../prac_02/name.txt", "w") as file:
    file.write(name)

# Read the name from the file and print a greeting
with open("../prac_02/name.txt", "r") as file:
    name = file.read()
    print(f"Hi {name}!")

# Read the first two numbers from numbers.txt and print their sum
with open("numbers.txt", "r") as file:
    numbers = [int(file.readline()) for _ in range(2)]
    print(sum(numbers))

# Read all numbers from numbers.txt and print their total
with open("numbers.txt", "r") as file:
    total = sum(int(line) for line in file)
    print(total)
