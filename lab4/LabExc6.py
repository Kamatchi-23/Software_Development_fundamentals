"""
Develop a program called Lab4Exc6 to achieve the following operations:
• Generate a random number of seed 10, n times (n is entered from keyboard).
• Then add only the even values
• Show the total of even values
"""

import random

n = int(input("Enter the number of input random numbers: "))
rand_int_lst, even_lst = [], []
for i in range(n):
    random.seed(10)
    rand_int_lst.append(random.randint(1, 1000))
print("List of ", n, " random integers of seed 10:", rand_int_lst)   
even_lst = [i for i in rand_int_lst if i%2 ==0]
print("Total of even values: ", sum(even_lst))