from lambdafun import is_adult

age =int(input("please enter your age : "))

if is_adult(age):
    print("eligible to vote")
else:
    while not is_adult(age):
        print("sorry next person please..")
        age =int(input("please enter your age : "))

    print("eligible to vote")

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


    
