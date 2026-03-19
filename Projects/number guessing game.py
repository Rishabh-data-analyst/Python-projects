import random

print(" Two Digit Number Guessing Game")

surprise_number = random.randrange(10, 99)    #to generate any number

while True:
    guess = int(input("Guess a number between 10 to 99"))   #ask user to guess the number

    if guess > surprise_number:                           #user guess is higher
        print("Surprise number is :", surprise_number)
        print("Your guess is higher than the number.")
    elif guess < surprise_number:                          #user guess is lower
        print("Surprise number is :", surprise_number)
        print("Your guess is lower than the number.")
    else:                                                  #correct guess by user
        print("Surprise number is :", surprise_number)
        print("Congratulations Your guess is correct")
        break

