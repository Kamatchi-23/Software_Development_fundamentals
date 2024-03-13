"""
Develop a program called Lab4Exc2 to achieve the following operations:
• Generate 20 random integers
• Store the values into an array
• Display the array
"""

import random

rand_int_lst=[]
rand_int_lst = random.sample(range(1, 1000), 20)

print(rand_int_lst)