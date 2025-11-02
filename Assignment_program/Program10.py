# Swap First and Last Characters
s = input("Enter a string: ")
result = ""

for i in range(len(s)):
    if i == 0:
        result += s[-1]
    elif i == len(s)-1:
        result += s[0]
    else:
        result += s[i]

print(result)