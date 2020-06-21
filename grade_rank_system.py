from grade import Grade

class GradeRankSystem:
    def __init__(self):
        self._grades = {}

    def read(self, grade_data_file):
        self._grades = {}
        with open(grade_data_file, 'rt', encoding='utf-8') as fo:
            data = fo.read()
            lines = data.strip().split('\n')

        num = 0
        for line in lines:
            num = num + 1
            self._grades[num] = Grade(line.strip())


        return len(self._grades)

    def sort_by_gid(self,order="asc"):
        if order == "asc":
            sorted_grades = sorted(self._grades.items())
        elif order == "des":
            sorted_grades = sorted(self._grades.items(),reverse=True)


        result = ""
        for key, item in sorted_grades:
            result = result + item.gid + ","
            result = result + item.stname + ","
            result = result + str(int(item.kor)) + ","
            result = result + str(int(item.eng)) + ","
            result = result + str(int(item.mat)) + ","
            result = result + str(int(item.gsum)) + ","
            result = result + str(item.avg) + "\n"
        return result.strip()
