import random

try:
    # Choose number of players
    while True:
        try:
            num_players = int(input("How many players? (1, 2, or 3): ").strip())
            if num_players in [1, 2, 3]:
                break
            print("Enter 1, 2, or 3.")
        except ValueError:
            print("Enter a valid integer (1, 2, or 3).")

    # Get player names
    players = []
    for i in range(num_players):
        name = input(f"Enter a name for player {i + 1}: ").strip()
        players.append(name)

    while True:
        goal = random.randint(20, 50)  # Target score
        print(f"\nThe goal is to reach {goal} points without going over\n")
        scores = {p: 0 for p in players}
        stopped = {p: False for p in players}
        quit_game = {p: False for p in players}
        turn = 0

        while True:
            # Find next player who hasn't quit or stopped
            active_players = [p for p in players if not stopped[p] and not quit_game[p]]
            if not active_players:
                print("\nAll players have stopped or quit. The game ends.\n")
                break
            current_player = players[turn % num_players]
            # Skip if player has quit or stopped
            if stopped[current_player] or quit_game[current_player]:
                turn += 1
                continue

            print(
                f"{current_player}'s turn. You now have {scores[current_player]} points and the goal is {goal}."
            )
            value = input(
                "enter '+' to roll again, '-' to hold, or 'q' to quit: "
            ).strip()
            if value == "+":
                num = random.randint(1, 15)  # "dice"
                print(f"You rolled {num} and now have a total of {scores[current_player] + num} points\n")
                scores[current_player] += num
                if scores[current_player] > goal:
                    print(f"BUST! {current_player} has {scores[current_player]} which went over\n")
                    scores[current_player] = 0
                    stopped[current_player] = True
            elif value == "-":
                print(f"{current_player} has held at {scores[current_player]} points!")
                stopped[current_player] = True
            elif value.lower() == "q":
                print(f"{current_player} has chosen to stop playing.")
                quit_game[current_player] = True
                stopped[current_player] = True
            else:
                print("Invalid choice, try again")
                continue

            # Check if all players have stopped
            if all(stopped.values()):
                # Calculate differences for all players
                diffs = {}
                for p in players:
                    if scores[p] <= goal:
                        diffs[p] = goal - scores[p]
                    else:
                        diffs[p] = float("inf")
                min_diff = min(diffs.values())
                winners = [p for p, diff in diffs.items() if diff == min_diff]
                if len(winners) == 1:
                    print(
                        f"\n{winners[0]} wins with {scores[winners[0]]} points, closest to the goal {goal}!\n"
                    )
                else:
                    print(
                        f"\nTie! {' and '.join(winners)} are equally close to the goal {goal}.\n"
                    )
                break

            turn += 1  # Next player's turn

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thanks for playing!")
            break
except KeyboardInterrupt:
    print("\nGame ended. Thanks for playing!")
