# Count the Number of Vowels in a string.

num1 = input('Enter the String: ')
count=0
num1 = num1.lower()
for ch in num1:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count+=1
print('number of vowels in the strings: ',count)