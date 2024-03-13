"""
Develop a program called Lab4Exc8 to achieve the following operations:
• Calculate the factorial of n (where n is entered from keyboard)
• Show the factorial of n
"""
import math

n = int(input("Enter of input number whose factorial has to be found:"))
fact = 1
if n > 0:
    for i in range(n):
        fact = fact * (i+1)
    print("Factorial using direct method:", math.factorial(n))
    print("Factorial using for loop:", fact)
elif n == 0:
    print("Factorial of 0 is:", fact)
else:
    print("Factorial of negative numbers cannot be computed")
