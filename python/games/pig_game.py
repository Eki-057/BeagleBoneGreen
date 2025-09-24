import random


def roll_turn(player: str) -> int:
    total = 0
    while True:
        num = random.randint(1, 6)
        total += num
        if num == 1:
            print(f"{player}: Sorry, you lost your points for this round!")
            return 0
        print(f"{player}: Total for this round: {total}")
        choice = input(f"{player}: Press r to roll again or h to hold: ")
        match choice:
            case "r":
                continue
            case "h":
                return total


def main() -> None:
    players = ["Player 1", "Player 2"]
    scores = {p: 0 for p in players}
    turn = 0

    while True:
        current_player = players[turn % 2]
        print(f"\n{current_player}'s turn. Current score: {scores[current_player]}")
        round_score = roll_turn(current_player)
        scores[current_player] += round_score
        print(f"{current_player} now has {scores[current_player]} points")
        if scores[current_player] >= 100:
            print(f"Congratulations {current_player}, you won with {scores[current_player]} points!")
            break
        input("Press 'Enter' to continue to the next player")
        turn += 1


main()
