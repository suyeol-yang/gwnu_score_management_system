class Grade:


    def __init__(self, data):
        items = data.split(',')

        self._gid = items[0]
        self._stname = items[1]
        self._kor = float(items[2])
        self._eng = float(items[3])
        self._mat = float(items[4])
        # self._sum = float(items[5])
        # self._avg = float(items[5])

    @property
    def gid(self):
        return self._gid

    @property
    def stname(self):
        return self._stname

    @property
    def kor(self):
        return self._kor

    @property
    def eng(self):
        return self._eng

    @property
    def mat(self):
        return self._mat

    @property
    def sum(self):
        return self._kor + self._eng + self._mat

    @property
    def avg(self):
        return (self._kor + self._eng + self._mat)/3
