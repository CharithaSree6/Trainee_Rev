from ArithCalculations import ArithCalculations
from AgeNotEnoughError import AgeNotEnoughError


n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
age=int(input('Enter age: '))
calc = ArithCalculations(n1,n2)

print(f'{calc.add()}')
print(f'{calc.sub()}')
print(f'{calc.mul()}')



try:
    if n2 ==0:
        raise ZeroDivisionError('n2 is 0')
    if age < 18:
        raise AgeNotEnoughError('you are minor')
except ZeroDivisionError as zde:
    print(f'{zde}')
except AgeNotEnoughError as anee:
    print(f'{anee}')
else:
    try:
        l1=[1,5,7,3]
        val = l1[1]
        res = calc.div()
    except ZeroDivisionError as zde:
        print(f'{zde} - 0 is a denminatore')

    except:
        print('Oop!!')
    else:
        print(val)
        print(res)
    finally:
        print('done !!')
