import json
import os
import random
import time

LEADERBOARD_FILE = "leaderboard.json"  # Filename for the leaderboard
TOP_N = 5  # Number of entries in the leaderboard


def load_leaderboard():
    """Load the leaderboard from file if it exists, otherwise return an empty list."""
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_leaderboard(leaderboard):
    """Save the leaderboard to file."""
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        json.dump(leaderboard, f, ensure_ascii=False, indent=2)


def update_leaderboard(leaderboard, username, score, streak, timer_seconds):
    """Add a new entry and sort the leaderboard."""
    leaderboard.append({
        "username": username,
        "score": score,
        "streak": streak,
        "timer_seconds": timer_seconds,
    })
    leaderboard.sort(key=lambda x: (-x["score"], -x["streak"]))
    return leaderboard[:TOP_N]


def print_leaderboard(leaderboard):
    """Print the leaderboard."""
    print("\n--- Top 5 Leaderboard ---")
    for i, entry in enumerate(leaderboard, 1):
        print(
            f"{i}. {entry['username']} - Correct: {entry['score']}, "
            f"Streak: {entry['streak']}, Time: {entry.get('timer_seconds', 30)} sec"
        )
    print("-------------------------\n")


def choose_table():
    """Let the user choose a table or random."""
    while True:
        choice = input(
            "Would you like to choose a table or use a random one? (type 'choose' or 'random'): "
        ).strip().lower()
        if choice == "choose":
            while True:
                try:
                    number = int(input("Enter a number between 1 and 10: "))
                    if 1 <= number <= 10:
                        print(f"You chose: {number}")
                        return True, number  # Use chosen table
                    print("Enter a number between 1 and 10.")
                except ValueError:
                    print("That is not an integer. Try again!")
        elif choice == "random":
            return False, None  # Use random
        else:
            print("Invalid response. Type 'choose' or 'random'.")


def play_game(username, timer_seconds, use_selected, number):
    total_correct = 0  # Total correct answers
    streak = 0  # Current streak
    max_streak = 0  # Highest streak
    start_time = time.time()  # Start time
    while True:
        if time.time() - start_time >= timer_seconds:
            break  # End if time is up
        number1 = number if use_selected else random.randint(1, 10)  # First number
        number2 = random.randint(1, 10)  # Second number
        correct_answer = number1 * number2  # Correct answer
        print(f"What is {number1} * {number2}?")
        while True:
            try:
                if time.time() - start_time >= timer_seconds:
                    break  # End if time is up
                answer = input("Answer: ")
                if time.time() - start_time >= timer_seconds:
                    break  # End if time is up
                answer = int(answer)
                if answer == correct_answer:
                    print("Correct answer!\n")
                    total_correct += 1  # Increase correct answers
                    streak += 1  # Increase streak
                    if streak > max_streak:
                        max_streak = streak  # Update max streak
                    break  # Move to next question
                print("Incorrect answer. Next question!\n")
                streak = 0  # Reset streak on wrong answer
                break  # Move to next question
            except ValueError:
                print("Please enter an integer.\n")
        if time.time() - start_time >= timer_seconds:
            break  # End if time is up
    print(f"\nTime is up! You got {total_correct} correct.")
    print(f"Your highest streak was: {max_streak}\n")
    return total_correct, max_streak  # Return results


def main():
    leaderboard = load_leaderboard()  # Load leaderboard
    print_leaderboard(leaderboard)  # Print leaderboard
    username = input("Enter your username: ")  # Get username
    use_selected, number = choose_table()  # Table choice
    while True:
        try:
            while True:
                try:
                    timer_seconds = int(input("How many seconds do you want to play? (e.g., 30): "))
                    if timer_seconds > 0:
                        break
                    print("Enter a positive integer for seconds.")
                except ValueError:
                    print("Enter a valid integer for seconds.")
            print(
                f"\nYou have {timer_seconds} seconds to answer as many questions as possible!"
            )
            score, max_streak = play_game(username, timer_seconds, use_selected, number)
            leaderboard = update_leaderboard(
                leaderboard, username, score, max_streak, timer_seconds
            )
            save_leaderboard(leaderboard)
            print_leaderboard(leaderboard)
            again = input("Do you want to play again? (y/n): ").strip().lower()
            if again == "y":
                same_user = input("Do you want to use the same username? (y/n): ").strip().lower()
                if same_user != "y":
                    username = input("Enter a new username: ")
                use_selected, number = choose_table()  # New table choice
            else:
                print("Thanks for playing!")
                break
        except KeyboardInterrupt:
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
