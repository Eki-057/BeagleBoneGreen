import random
import json
import os

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
        print(f"{i}. {entry['username']} - {entry['guesses']} gissningar")
    print("-----------------------\n")

def guess(a, b):
    username = input("Ange ditt användarnamn: ").strip()
    while not username:
        username = input("Användarnamn kan inte vara tomt. Ange ditt användarnamn: ").strip()

    num = random.randint(a, b)
    attempts = 0
    congrats = [
        "Bra jobbat!", "Fantastiskt!", "Du klarade det!", "Snyggt gissat!", "Imponerande!", "Du är en mästare!"
    ]
    while True:
        gissning_input = input(f"Gissa ett nummer mellan {a} och {b}: ")
        if not gissning_input.strip():
            print("Du måste skriva ett nummer!")
            continue
        try:
            gissning = int(gissning_input)
        except ValueError:
            print("Du måste skriva ett giltigt nummer!")
            continue
        attempts += 1
        if gissning == 69 and random.random() < 0.03:
            print("Nice.")
            continue
        if gissning > num:
            print("Ditt nummer var för stort")
        elif gissning < num:
            print("Ditt nummer var för litet")
        else:
            print(f"{random.choice(congrats)} {username}, du gissade rätt på {attempts} försök!")
            # Save highscore
            highscores = load_highscores()
            highscores.append({"username": username, "guesses": attempts})
            highscores.sort(key=lambda x: x["guesses"])
            # Only keep top 5 scores
            if len(highscores) > 5:
                highscores = highscores[:5]
            save_highscores(highscores)
            show_top5(highscores)
            break

guess(1, 400)