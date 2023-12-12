import random

number = random.randint(1,100)
guess=int(input("guess the number: "))

while not guess==number:
    if guess<number:
        print("too low")
    else:
        print("too high")

    guess=int(input("try again !! : "))


print("congrats you guessed correct")
