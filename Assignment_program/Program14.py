# Create a script using Python's range function to print all even numbers between 1 and 20.
num=int(input("Enter a number: "))
for num in range(1, 21):
    if num % 2 == 0:
        print(num)