# Slice Characters of user choices and display error message if not possible

s = input("Enter a string: ")
start = int(input("Start index: "))
end = int(input("End index: "))

if start < end and end <= len(s):
    print("Result:", s[start:end])
else:
    print("Error: Cannot slice with given indexes")