# Task 1: Write a function in Python that calculates and returns the factorial of a number provided as an argument.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# take input
num = int(input("Enter a number: "))

print("Factorial:", factorial(num))