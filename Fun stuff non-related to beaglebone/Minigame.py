import random
def guess():
    num = random.randint(1, 100)
    attempts = 0
    while True:
        gissning_input = input("Gissa ett nummer mellan ett och hundra: ")
        if not gissning_input.strip():
            print("Du måste skriva ett nummer!")
            continue
        try:
            gissning = int(gissning_input)
        except ValueError:
            print("Du måste skriva ett giltigt nummer!")
            continue
        attempts += 1
        if gissning > num:
            print("Ditt nummer var för stort")
        elif gissning < num:
            print("Ditt nummer var för litet")
        else:
            print(f"Grattis, du gissade rätt på {attempts} försök")
            break

guess()