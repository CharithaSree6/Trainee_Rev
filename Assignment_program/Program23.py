#Program to print duplicates from a list of integers.

numbers = [1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 5]

for num in numbers:
    if numbers.count(num) > 1:
        print(num)