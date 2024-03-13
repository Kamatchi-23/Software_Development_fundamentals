"""
Develop a program called Lab4Exc9 to achieve the following operations:
• Generates a random integer between 1 and 10 (inclusive). [Never print this number]
• Keep guessing the correct random integer.
• If your guess is correct, print “Success, secret number = <the number value>” and terminate the program
• If your guess is incorrect print “Sorry – try again!”, then keep trying
"""
import random

ran_int = random.randint(1,10)
while(True):
    your_guess = int(input("Guess the random integer between 1 and 10 (inclusive): "))
    if your_guess == ran_int:
        print("Success, secret number = ", ran_int)
        break
    else:
        print("Sorry - try again!")

