"""
Develop a program called Lab4Exc1 to achieve the following operations:
• Display all numbers from 1 to 10
• Display the square roots of each number
• Display the exponents of each number
• Show all displays in a tabular formatimport math
"""
import math

i = 1
print("+----------+----------+----------+")
print("| i        | sqrt(i)  | square(i)|")
print("+----------+----------+----------+")
format_row = "{:3} {:13} {:14}"
for i in range(1,11):
    print(format_row.format(i, round(math.sqrt(i),2), int(math.pow(i,2))))
print("+----------+----------+----------+")
