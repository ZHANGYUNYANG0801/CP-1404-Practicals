def main():
    MIN_LENGTH = 6
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(min_length):
    """Prompt user for a valid password."""
    password = input("Enter your password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print('*' * len(password))

if __name__ == "__main__":
    main()
