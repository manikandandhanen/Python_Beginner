answer = 7

print("Please guess the number between 1 to 10")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry you have not guessed correctly")
else:
    print("You got it first time")
