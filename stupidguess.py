import random

# generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# set the number of guesses to 0
num_guesses = 0

# loop until the user guesses the correct number or runs out of guesses
while num_guesses < 6:
    # ask the user to guess the number
    guess = int(input("Guess a number between 1 and 20: "))

    # increment the number of guesses
    num_guesses += 1

    # compare the user's guess with the secret number
    if guess == secret_number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break
    elif guess < secret_number:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")

# if the user runs out of guesses, reveal the secret number
if num_guesses == 6:
    print("Sorry, you ran out of guesses. The secret number was", secret_number)
