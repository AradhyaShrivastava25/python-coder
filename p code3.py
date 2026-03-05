import random
secret = random.randint(1, 10)
guess = int(input("Guess a number: "))
if guess > secret:
    print("Too high!")
elif guess < secret:
    print("Too low!")
else:
    print("Correct!")
