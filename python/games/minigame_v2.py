import random


def guess(lower: int, upper: int):
    num = random.randint(lower, upper)
    attempts = 0
    while True:
        guess_input = input(f"Guess a number between {lower} and {upper}: ")
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


guess(1, 400)
