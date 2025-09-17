import random

try:
    # Choose number of players
    while True:
        try:
            num_players = int(input("Hur många spelare? (1, 2 eller 3): ").strip())
            if num_players in [1, 2, 3]:
                break
            else:
                print("Ange 1, 2 eller 3.")
        except ValueError:
            print("Ange ett giltigt heltal (1, 2 eller 3).")

    # Get player names
    players = []
    for i in range(num_players):
        name = input(f"Ange namn för spelare {i+1}: ").strip()
        players.append(name)

    while True:
        goal = random.randint(20, 50)  # Target score
        print(f"\nMålet är att nå {goal} poäng utan att gå över\n")
        scores = {p: 0 for p in players}
        stopped = {p: False for p in players}
        quit_game = {p: False for p in players}
        turn = 0

        while True:
            # Find next player who hasn't quit or stopped
            active_players = [p for p in players if not stopped[p] and not quit_game[p]]
            if not active_players:
                print("\nAlla spelare har slutat eller stannat. Spelet avslutas.\n")
                break
            current_player = players[turn % num_players]
            # Skip if player has quit or stopped
            if stopped[current_player] or quit_game[current_player]:
                turn += 1
                continue

            print(f"{current_player}s tur. Du har nu {scores[current_player]} poäng och målet är {goal}.")
            val = input("skriv '+' för att kasta på nytt, '-' för att stanna, eller 'q' för att sluta: ").strip()
            if val == "+":
                num = random.randint(1, 15)  # "dice"
                print(f"Du kastade {num} och har nu totalt {scores[current_player] + num} poäng\n")
                scores[current_player] += num
                if scores[current_player] > goal:
                    print(f"BUST! {current_player} har {scores[current_player]} vilket gick över \n")
                    scores[current_player] = 0
                    stopped[current_player] = True
            elif val == "-":
                print(f"{current_player} har stannat på {scores[current_player]} poäng!")
                stopped[current_player] = True
            elif val.lower() == "q":
                print(f"{current_player} har valt att sluta spela.")
                quit_game[current_player] = True
                stopped[current_player] = True
            else:
                print("ogiltigt val, försök igen")
                continue

            # Check if all players have stopped
            if all(stopped.values()):
                # Calculate differences for all players
                diffs = {}
                for p in players:
                    if scores[p] <= goal:
                        diffs[p] = goal - scores[p]
                    else:
                        diffs[p] = float('inf')
                min_diff = min(diffs.values())
                winners = [p for p, d in diffs.items() if d == min_diff]
                if len(winners) == 1:
                    print(f"\n{winners[0]} vinner med {scores[winners[0]]} poäng, närmast målet {goal}!\n")
                else:
                    print(f"\nOavgjort! {' och '.join(winners)} är lika nära målet {goal}.\n")
                break

            turn += 1  # Next player's turn

        play_again = input("Vill ni spela igen? (j/n): ")
        if play_again.lower() != 'j':
            print("Tack för att ni spelade!")
            break
except KeyboardInterrupt:
    print("\nSpelet avslutat. Tack för att ni spelade!")