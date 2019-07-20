import random

number = random.randint(1, 10)
tries = 1

uname = input("HELLO,What is your name?")

print("Hello", uname + ".")

question = input("Would you like to Play Game? [y/n]")
if question == "n":
    print("oh..OKAY")

if question == "y":
    print("I'm thinkng of a Number Between 1 & 10")
    guess = int(input("Have a Guess: "))
    if guess > number:
        print("Guess Lower..")
if guess < number:
    print("Guess Higher..")
while guess != number:
    tries += 1
    guess = int(input("Try Again: "))
    if guess < number:
        print("Guess Higher")
if guess == number:
    print("You're Right! YOU WIN! The Number was", number, \
          "and it only", tries, "tries!")
