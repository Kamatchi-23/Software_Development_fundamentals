"""Develop a program called Lab4Exc5 to achieve the following operations:
• Add all even numbers from 1 up to n and prints the total, where the value of n is entered from keyboard.
• The program should print the even-sum of every entered n
NOTES:
• The program stops when -1 is entered from keyboard.
"""
while(True):
    even_lst=[]
    n = int(input("Enter the input number: "))
    if n != -1:
        even_lst = [i for i in range(1, n+1) if i%2 == 0]
        print("The sum of even numbers from 1 to ", n, " is:", sum(even_lst))
    else:
        print("Good Bye")
        break