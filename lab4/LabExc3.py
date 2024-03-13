"""
Develop a program called Lab4Exc3 to achieve the following operations:
• Repeat-print out n stars on one line (where the value of n is captured from keyboard).
NOTES:
• Don't forget to terminate the previous line.
• The program should terminate when n is zero.
"""

while(True):
    n = int(input("Enter a number of stars to be printed:"))
    if n == 0:
        break
    else:
        print("*" * n)