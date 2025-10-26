num = int(input("enter the first number:"))
num_len=len(str(num))
temp = num
sum=0
while(num>0):
    rem=num%10
    sum = sum+rem ** num_len
    num=num//10
    temp==sum
    if sum==num:
        print('the number is armstrong')
    else:
        print('the number is not armstrong')

