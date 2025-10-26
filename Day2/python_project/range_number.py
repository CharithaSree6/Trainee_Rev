terms=int(input('enter the number: '))
sum=0
for num in range(1,terms+1):
    sum += (sum*num)
print(f'sum is:{sum}')