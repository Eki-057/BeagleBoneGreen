import random
def guess():
    num = random.randint(1, 100)
    attempts = 0
    gissning = int(input("Gissa ett nummer mellan ett och hundra: "))
    while True:
        attempts += 1
        if gissning > num:
            print("Ditt nummer var för stort")
        elif gissning < num:
            print("Ditt nummer var för litet")
        else:
            print(f"Grattis, du gissade rätt på {attempts} försök")
            break
        gissning = int(input("Gissa igen: "))

guess()