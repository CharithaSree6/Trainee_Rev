#from StudDetails import StudentDetail
from oop.StudDetails import StudentDetail
from StudExcurr import StudExcurr

ccode = input('ccode: ')
cname = input('cname: ')

rollno = int(input('roll no: '))
sname = input('Name: ')
m1=int(input('Mark M1: '))
m2 = int(input('Mark M2: '))
m3 = int(input('Mark M3: '))
exm1=int(input('ex Mark M1: '))
exm2 = int(input('ex Mark M2: '))

stud = StudExcurr(ccode, cname, rollno, sname, m1, m2, m3,exm1, exm2)

print(f'{stud.display()[0]} \t {stud.display()[1]}')
print(f'Rollno: {stud.get_rollno()} \nName: {stud.get_sname()} \nTotal: {stud.calc_tot()} \n'
      f'Average: {stud.calc_avg()}')
print(f'{stud.calc_extot()}')
