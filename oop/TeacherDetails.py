from collage import Collage

class TeacherDetails(Collage):
    def __init__(self, ccode, cname, empid, tname, dept):
        Collage.__init__(self, ccode, cname)  # direct call
        self.empid = empid
        self.tname = tname
        self.dept = dept

    def Teachers_display(self):
        print(f'{self._ccode} \t {self._cname} \n{self.empid} \n{self.tname} \n{self.dept}')
