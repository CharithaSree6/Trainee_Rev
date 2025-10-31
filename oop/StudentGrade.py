#from StudDetails import StudentDetail
# from oop.StudDetails import StudentDetail
from StudExcurr import StudExcurr
from oop.TeacherDetails import TeacherDetails
from FinalEval import FInalEval

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

'''print(f'{stud.display()[0]} \t {stud.display()[1]}')
print(f'Rollno: {stud.get_rollno()} \nName: {stud.get_sname()} \nTotal: {stud.calc_tot()} \n'
      f'Average: {stud.calc_avg()}')
print(f'{stud.calc_extot()}')'''


empid = int(input('empid: '))
tname = input('Name: ')
dept=int(input('dept: '))

'''teacher = TeacherDetails(ccode, cname, empid, tname, dept)
teacher.display()'''

feedbackfromteacher = input('enter the feedback: ')
finaleval = FInalEval(ccode, cname, rollno, sname, m1, m2, m3, exm1, exm2, empid, tname, dept, feedbackfromteacher)
print(f'{finaleval.Collage_display()[0]}\t {finaleval.Collage_display()[1]}')
print( f'{finaleval.get_rollno()}\n'
      f'{finaleval.get_sname()}\n'
      f'{finaleval.calc_tot()}\n'
      f'{finaleval.calc_avg()}\n'
      f'{finaleval.calc_extot()}\n')
finaleval.Teachers_display()
print(f'{finaleval.feedbackfromteacher}')
