import random


def guess():
    num = random.randint(1, 100)
    attempts = 0
    while True:
        guess_input = input("Guess a number between one and one hundred: ")
        if not guess_input.strip():
            print("You must enter a number!")
            continue
        try:
            guess_value = int(guess_input)
        except ValueError:
            print("You must enter a valid number!")
            continue
        attempts += 1
        if guess_value > num:
            print("Your number was too high")
        elif guess_value < num:
            print("Your number was too low")
        else:
            print(f"Congratulations, you guessed correctly in {attempts} attempts")
            break


guess()
