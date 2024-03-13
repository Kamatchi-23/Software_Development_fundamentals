"""
Develop a program called Lab4Exc4 to achieve the following operations:
• Read n integers from keyboard.
• Display the min and max values entered.
NOTES:
• The program ends when -1 is entered.
"""

while (True):
    n = int(input("Enter the total number of integers to read:"))
    if n != -1:
        int_lst = []
        for i in range(n):
            print("Enter the ", i+1, " integer:")
            ith = int(input())
            int_lst.append(ith)
        print("Minimum of the ", n, " integers entered:", min(int_lst))
        print("Maximum of the ", n, " integers entered:", max(int_lst))
    else:
        print("Good Bye")
        break