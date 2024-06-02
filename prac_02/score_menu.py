import score  # Importing the get_score_result function from score.py

def get_valid_score():
    """Prompt the user to enter a valid score (0-100 inclusive) and return it."""
    while True:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def print_stars(score):
    """Print as many stars as the score."""
    print("*" * int(score))

def main():
    score_value = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Choose an option: ").strip().upper()

        if choice == 'G':
            score_value = get_valid_score()
        elif choice == 'P':
            result = score.get_score_result(score_value)
            print(f"Result: {result}")
        elif choice == 'S':
            print_stars(score_value)
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

