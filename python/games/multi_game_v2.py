import random
import time
import json
import os

LEADERBOARD_FILE = "leaderboard.json"  # Filename for the leaderboard
TOP_N = 5  # Number of entries in the leaderboard

def load_leaderboard():
    # Load the leaderboard from file if it exists, otherwise return an empty list
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_leaderboard(leaderboard):
    # Save the leaderboard to file
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        json.dump(leaderboard, f, ensure_ascii=False, indent=2)

def update_leaderboard(leaderboard, username, score, streak, timer_seconds):
    # Add a new entry and sort the leaderboard
    leaderboard.append({
        "username": username,
        "score": score,
        "streak": streak,
        "timer_seconds": timer_seconds
    })
    leaderboard.sort(key=lambda x: (-x["score"], -x["streak"]))
    return leaderboard[:TOP_N]

def print_leaderboard(leaderboard):
    # Print the leaderboard
    print("\n--- Top 5 Leaderboard ---")
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry['username']} - Rätt: {entry['score']}, Streak: {entry['streak']}, Tid: {entry.get('timer_seconds', 30)} sek")
    print("-------------------------\n")

def choose_table():
    # Let the user choose a table or random
    while True:
        val = input("Vill du välja tabell eller slumpmässigt valt? (skriv 'val' eller 'random'):").strip().lower()
        if val == 'val':
            while True: 
                try:
                    number = int(input("Skriv ett nummer mellan 1 och 10: "))
                    if 1 <= number <= 10:
                        print(f"Du valde: {number}")
                        return True, number  # Use chosen table
                    else:
                        print("Skriv ett nummer mellan 1 och 10.")
                except ValueError:
                    print("Det är inte ett heltal. Försök på nytt!")
        elif val == 'random':
            return False, None  # Use random
        else:
            print("Ogiltigt svar. Skriv: 'val' eller 'random'.")

def play_game(username, timer_seconds, anvand_val, number):
    total_ratt = 0  # Total correct answers
    streak = 0      # Current streak
    max_streak = 0  # Highest streak
    start_time = time.time()  # Start time
    while True:
        if time.time() - start_time >= timer_seconds:
            break  # End if time is up
        tal1 = number if anvand_val else random.randint(1, 10)  # First number
        tal2 = random.randint(1, 10)  # Second number
        rätt_svar = tal1 * tal2  # Correct answer
        print(f"Vad är {tal1} * {tal2}?")
        while True:
            try:
                if time.time() - start_time >= timer_seconds:
                    break  # End if time is up
                svar = input("Svar: ")
                if time.time() - start_time >= timer_seconds:
                    break  # End if time is up
                svar = int(svar)
                if svar == rätt_svar:
                    print("Rätt svar!\n")
                    total_ratt += 1  # Increase correct answers
                    streak += 1      # Increase streak
                    if streak > max_streak:
                        max_streak = streak  # Update max streak
                    break  # Move to next question
                else:
                    print("Fel svar. Nästa fråga!\n")
                    streak = 0  # Reset streak on wrong answer
                    break  # Move to next question
            except ValueError:
                print("Skriv ett heltal, tack.\n")
        if time.time() - start_time >= timer_seconds:
            break  # End if time is up
    print(f"\nTiden är slut! Du fick {total_ratt} rätt.")
    print(f"Din högsta streak var: {max_streak}\n")
    return total_ratt, max_streak  # Return results

def main():
    leaderboard = load_leaderboard()  # Load leaderboard
    print_leaderboard(leaderboard)    # Print leaderboard
    username = input("Ange ditt användarnamn: ")  # Get username
    anvand_val, number = choose_table()           # Table choice
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
            score, max_streak = play_game(username, timer_seconds, anvand_val, number)  # Play the game
            leaderboard = update_leaderboard(leaderboard, username, score, max_streak, timer_seconds)  # Update leaderboard
            save_leaderboard(leaderboard)  # Save leaderboard
            print_leaderboard(leaderboard) # Print leaderboard
            again = input("Vill du spela igen? (y/n): ").strip().lower()
            if again == "y":
                same_user = input("Vill du använda samma användarnamn? (y/n): ").strip().lower()
                if same_user != "y":
                    username = input("Ange nytt användarnamn: ")
                anvand_val, number = choose_table()  # New table choice
            else:
                print("Tack att du spelade!")
                break
        except KeyboardInterrupt:
            print("\nTack att du spelade!")
            break

if __name__ == "__main__":
    main()