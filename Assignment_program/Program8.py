# Remove Duplicates from String
string ="programming"
result = ""

for char in string:
    if char not in result:
        result += char

print("String without duplicates:", result)