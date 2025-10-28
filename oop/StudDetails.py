
from oop.collage import Collage


class StudentDetail(Collage):
    def __init__(self, ccode, cname, rollno, sname, m1, m2, m3):
        super().__init__(ccode,cname)
        self.__rollno = rollno
        self.__sname = sname
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3


    def get_rollno(self):
        return self.__rollno
    def set_rollno(self, rollno):
        self.__rollno = rollno

    def get_sname(self):
        return self.__sname
    def set_sname(self, sname):
       self.__sname = sname

    def get_m1(self):
        return self.__m1
    def set_m1(self, m1):
        self.__m1 = m1

    def get_m2(self):
        return self.__m2
    def set_m2(self, m2):
        self.__m2 = m2

    def get_m3(self):
        return self.__m3
    def set_m3(self, m3):
        self.__m3 = m3

    def get_exm1(self):
        return self.__exm1
    def set_exm1(self, exm1):
        self.__exm1 = exm1

    def get_exm2(self):
        return self.__exm2
    def set_exm2(self, exm2):
        self.__exm2 = exm2

    def calc_tot(self):
        return self.__m1 + self.__m2 + self.__m3

    def calc_avg(self):
        return self.calc_tot() / 3
