import random

secret_number = random.randint(1, 10)

guess = int(input("Guess the number from 1 to 10: "))

if guess == secret_number:
    print("Correct!")

elif guess > secret_number:
    print("Too high!")

else:
    print("Too low!")
