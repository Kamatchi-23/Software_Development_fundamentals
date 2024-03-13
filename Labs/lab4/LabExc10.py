"""
Develop a program called Lab4Exc10 to achieve the following operations:
• Calculate and print the values of a Fibonacci series on separate lines.
NOTES:
• First number is 1
• Second number is 1
• Last Fibonacci number n [ n is entered from keyboard]
"""

n = int(input("Enter the number whose fibonacci series has to be found: "))
i = 1
j = 1
fib = 0
print(i, j, sep='\n')
for k in range(0, n-2):
    fib = i + j
    i = j
    j = fib
    print(fib)

