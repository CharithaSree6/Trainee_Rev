class Collage:
    def __init__(self, ccode, cname):
        self._ccode = ccode
        self._cname = cname


    def get_ccode(self):
        return self._ccode

    def get_cname(self):
        return self._cname


    def Collage_display(self):
        return self._ccode, self._cname
