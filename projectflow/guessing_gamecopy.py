import random

answer = random.randint(1,10)

print(answer)
print("Please guess a number between 1 and 10: ")
guess = int(input())


while guess != answer:
    if guess < answer:
        print("Please guess higher")

    elif guess > answer:
        print("Please guess lower")

    print("you've guessed incorrectly")
    print("Try again and guess a number between 1 and 10: ")
    guess = int(input())
else:
    print("You've guessed correctly!")




