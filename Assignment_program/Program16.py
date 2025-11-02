# Difference between Sums of Odd and Even Digits in numbers

num = input("Enter a number: ")

odd_sum = 0
even_sum = 0

for ch in num:      # loop through each digit
    digit = int(ch)
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

print("Difference =", odd_sum - even_sum)
