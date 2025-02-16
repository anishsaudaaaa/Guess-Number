import random

top_of_range =input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a positive integer")
        quit()
else:
    print("Please type the number next time...")
    quit()

random_number = random.randint( 0,top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type the number next time...")
        continue

    if user_guess == random_number:
        print("You guessed right number!")
        break
    elif user_guess > random_number:
        print("You guessed higher number!")
    else:
        print("You guessed lower number!")

print("You got it in", guesses, "guesses")
