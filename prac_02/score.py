import random


def get_score_result(score):
    """Determine the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    # Ask the user for their score and print the result
    user_score = float(input("Enter your score: "))
    user_result = get_score_result(user_score)
    print(f"Your result: {user_result}")

    # Generate a random score and print the result
    random_score = random.randint(0, 100)
    random_result = get_score_result(random_score)
    print(f"Random score: {random_score} - Result: {random_result}")


if __name__ == "__main__":
    main()
