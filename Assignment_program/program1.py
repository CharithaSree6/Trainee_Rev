from operator import truediv
# Print all Prime Numbers in an Interval.

num1 = int(input('Enter a start number: '))
num2 = int(input('Enter a end  number: '))
print(f'prime numbers between{num1} and {num2} are:')

for num in range(num1, num2+1):
    if num > 1:
        is_prime=True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime=False
        if is_prime:
            print(num)
