import random

def kasta(player):
    total = 0
    while True:
        num = random.randint(1, 6)
        total += num
        if num == 1:
            print(f"{player}: Sorry, du tappade dina poäng för denna runda!")
            return 0
        print(f"{player}: Summa för detta varv: {total}")
        val = input(f"{player}: Tryck på k för att kasta på nytt eller s för att spara: ")
        match val:
            case "k":
                continue
            case "s":
                return total

def main():
    players = ["Spelare 1", "Spelare 2"]
    scores = {p: 0 for p in players}
    turn = 0

    while True:
        current_player = players[turn % 2]
        print(f"\n{current_player}s tur. Nuvarande poäng: {scores[current_player]}")
        round_score = kasta(current_player)
        scores[current_player] += round_score
        print(f"{current_player} har nu {scores[current_player]} poäng")
        if scores[current_player] >= 100:
            print(f"Grattis {current_player}, du vann med {scores[current_player]} poäng!")
            break
        input("Tryck 'Enter' för att fortsätta till nästa spelare")
        turn += 1

main()