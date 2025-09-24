import json
import os
import random

HIGHSCORE_FILE = "highscores.txt"


def load_highscores():
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception:
            return []


def save_highscores(highscores):
    with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(highscores, f, ensure_ascii=False, indent=2)


def show_top5(highscores):
    print("\n--- Top 5 Highscores ---")
    for i, entry in enumerate(highscores[:5], 1):
        print(f"{i}. {entry['username']} - {entry['guesses']} guesses")
    print("-----------------------\n")


def guess(lower: int, upper: int):
    username = input("Enter your username: ").strip()
    while not username:
        username = input("Username cannot be empty. Enter your username: ").strip()

    num = random.randint(lower, upper)
    attempts = 0
    congrats = [
        "Great job!",
        "Fantastic!",
        "You did it!",
        "Nice guess!",
        "Impressive!",
        "You are a champion!",
    ]
    while True:
        guess_input = input(f"Guess a number between {lower} and {upper}: ")
        if not guess_input.strip():
            print("You must enter a number!")
            continue
        try:
            guess_value = int(guess_input)
        except ValueError:
            print("You must enter a valid number!")
            continue
        attempts += 1
        if guess_value == 69 and random.random() < 0.03:
            print("Nice.")
            continue
        if guess_value > num:
            print("Your guess was too high")
        elif guess_value < num:
            print("Your guess was too low")
        else:
            print(f"{random.choice(congrats)} {username}, you guessed correctly in {attempts} attempts!")
            highscores = load_highscores()
            highscores.append({"username": username, "guesses": attempts})
            highscores.sort(key=lambda x: x["guesses"])
            if len(highscores) > 5:
                highscores = highscores[:5]
            save_highscores(highscores)
            show_top5(highscores)
            break


guess(1, 400)
