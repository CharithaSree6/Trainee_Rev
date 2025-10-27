
def calculate(m1,m2,m3):
    total = m1+m2+m3
    avg = total/3
    return total,avg
m1=int(input("enter the first number"))
m2=int(input("enter the second number"))
m3=int(input("enter the third number"))
total,avg=calculate(m1,m2,m3)
print(f'total is: {total},average is: {avg}')
