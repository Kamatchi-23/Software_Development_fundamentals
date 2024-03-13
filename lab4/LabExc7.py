"""
Develop a program called Lab4Exc7 to achieve the following operations:
• Read characters from keyboard until dot (.) is entered
• Count the number of vowels entered
• Uppercase and Lowercase vowels should be counted
• Display the total vowel count
NOTES:
• The program stops when . Is entered from keyboard
"""
ipt_lst, vow_lst = [], []
while (True):
    
    inpt = input()
    if inpt != '.':
        ipt_lst.append(inpt)
    else:
        break

print("Input characters are: ", ipt_lst)
vow_lst = [charac for charac in ipt_lst if charac.lower()[0] in ['a', 'e', 'i', 'o', 'u']]
print("Total vowel count: ", len(vow_lst))