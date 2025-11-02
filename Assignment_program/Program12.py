# Concatenate Characters of user choices and display error message if not possible
s = input("Enter a string: ")
i = int(input("Enter first index: "))
j = int(input("Enter second index: "))

if i < len(s) and j < len(s):
    result = s[i] + s[j]
    print("Concatenated result:", result)
else:
    print("Error: Invalid indexes")