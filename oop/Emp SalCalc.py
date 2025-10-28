from oop.Employee import Employee


empid = int(input('Emp id:'))
ename = input('Employee name:')
bp = float(input('Basic pay:'))

employee = Employee(empid, ename, bp)

print(f'Emp id : {empid} \nName : {ename} \n' f'Gross pay: {employee.calc_grosspay()} \n'
f' Net pay : {employee.calc_netpay()}')
