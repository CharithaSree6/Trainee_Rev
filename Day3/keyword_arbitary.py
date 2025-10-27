


def add(**nums):
    print("Received nums:",(nums))
    res = nums['fn'] + nums['sn'] + nums['tn']
    return res

n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))

print("Sum:",add(fn=n1,sn=n2,tn=n3))