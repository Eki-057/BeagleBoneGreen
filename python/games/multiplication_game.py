import json
import os
import random
import time

LEADERBOARD_FILE = "leaderboard.json"
TIMER_SECONDS = 30
TOP_N = 5


def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        json.dump(leaderboard, f, ensure_ascii=False, indent=2)


def update_leaderboard(leaderboard, username, score, streak, timer_seconds):
    leaderboard.append({
        "username": username,
        "score": score,
        "streak": streak,
        "timer_seconds": timer_seconds,
    })
    leaderboard.sort(key=lambda x: (-x["score"], -x["streak"]))
    return leaderboard[:TOP_N]


def print_leaderboard(leaderboard):
    print("\n--- Top 5 Leaderboard ---")
    for i, entry in enumerate(leaderboard, 1):
        print(
            f"{i}. {entry['username']} - Correct: {entry['score']}, "
            f"Streak: {entry['streak']}, Time: {entry.get('timer_seconds', TIMER_SECONDS)} sec"
        )
    print("-------------------------\n")


def play_game(username, timer_seconds):
    total_correct = 0
    streak = 0
    max_streak = 0
    start_time = time.time()
    while True:
        if time.time() - start_time >= timer_seconds:
            break
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        correct_answer = number1 * number2
        print(f"What is {number1} * {number2}?")
        while True:
            try:
                if time.time() - start_time >= timer_seconds:
                    break
                answer = input("Answer: ")
                if time.time() - start_time >= timer_seconds:
                    break
                answer = int(answer)
                if answer == correct_answer:
                    print("Correct answer!\n")
                    total_correct += 1
                    streak += 1
                    if streak > max_streak:
                        max_streak = streak
                    break  # Move to next question
                print("Incorrect answer. Next question!\n")
                streak = 0
                break  # Move to next question
            except ValueError:
                print("Please enter an integer.\n")
        if time.time() - start_time >= timer_seconds:
            break
    print(f"\nTime is up! You got {total_correct} correct.")
    print(f"Your highest streak was: {max_streak}\n")
    return total_correct, max_streak


def main():
    leaderboard = load_leaderboard()
    print_leaderboard(leaderboard)
    username = input("Enter your username: ")
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
            score, max_streak = play_game(username, timer_seconds)
            leaderboard = update_leaderboard(leaderboard, username, score, max_streak, timer_seconds)
            save_leaderboard(leaderboard)
            print_leaderboard(leaderboard)
            again = input("Do you want to play again? (y/n): ").strip().lower()
            if again == "y":
                same_user = input("Do you want to use the same username? (y/n): ").strip().lower()
                if same_user != "y":
                    username = input("Enter a new username: ")
            else:
                print("Thanks for playing!")
                break
        except KeyboardInterrupt:
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
