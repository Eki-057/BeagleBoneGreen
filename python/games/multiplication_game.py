import random
import time
import json
import os

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
        "timer_seconds": timer_seconds
    })
    leaderboard.sort(key=lambda x: (-x["score"], -x["streak"]))
    return leaderboard[:TOP_N]

def print_leaderboard(leaderboard):
    print("\n--- Top 5 Leaderboard ---")
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry['username']} - Rätt: {entry['score']}, Streak: {entry['streak']}, Tid: {entry.get('timer_seconds', TIMER_SECONDS)} sek")
    print("-------------------------\n")

def play_game(username, timer_seconds):
    total_ratt = 0
    streak = 0
    max_streak = 0
    start_time = time.time()
    while True:
        if time.time() - start_time >= timer_seconds:
            break
        tal1 = random.randint(1, 10)
        tal2 = random.randint(1, 10)
        rätt_svar = tal1 * tal2
        print(f"Vad är {tal1} * {tal2}?")
        while True:
            try:
                if time.time() - start_time >= timer_seconds:
                    break
                svar = input("Svar: ")
                if time.time() - start_time >= timer_seconds:
                    break
                svar = int(svar)
                if svar == rätt_svar:
                    print("Rätt svar!\n")
                    total_ratt += 1
                    streak += 1
                    if streak > max_streak:
                        max_streak = streak
                    break  # Move to next question
                else:
                    print("Fel svar. Nästa fråga!\n")
                    streak = 0
                    break  # Move to next question
            except ValueError:
                print("Skriv ett heltal, tack.\n")
        if time.time() - start_time >= timer_seconds:
            break
    print(f"\nTiden är slut! Du fick {total_ratt} rätt.")
    print(f"Din högsta streak var: {max_streak}\n")
    return total_ratt, max_streak

def main():
    leaderboard = load_leaderboard()
    print_leaderboard(leaderboard)
    username = input("Ange ditt användarnamn: ")
    while True:
        try:
            while True:
                try:
                    timer_seconds = int(input("Hur många sekunder vill du spela? (t.ex. 30): "))
                    if timer_seconds > 0:
                        break
                    else:
                        print("Ange ett positivt heltal för sekunder.")
                except ValueError:
                    print("Ange ett giltigt heltal för sekunder.")
            print(f"\nDu har {timer_seconds} sekunder på dig att svara på så många tal som möjligt!")
            score, max_streak = play_game(username, timer_seconds)
            leaderboard = update_leaderboard(leaderboard, username, score, max_streak, timer_seconds)
            save_leaderboard(leaderboard)
            print_leaderboard(leaderboard)
            again = input("Vill du spela igen? (y/n): ").strip().lower()
            if again == "y":
                same_user = input("Vill du använda samma användarnamn? (y/n): ").strip().lower()
                if same_user != "y":
                    username = input("Ange nytt användarnamn: ")
            else:
                print("Tack att du spelade!")
                break
        except KeyboardInterrupt:
            print("\nTack att du spelade!")
            break

if __name__ == "__main__":
    main()