import math

i = 1
print("+----------+----------+----------+")
print("| i        | sqrt(i)  | square(i)|")
print("+----------+----------+----------+")
format_row = "{:3} {:13} {:14}"
for i in range(1,11):
    print(format_row.format(i, round(math.sqrt(i),2), int(math.pow(i,2))))
print("+----------+----------+----------+")
