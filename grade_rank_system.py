from grade import Grade


def key_avg(item):
    return item[1].avg


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

    def _make_grades_string(self,order_key,order_way,grades):
        rank_asc = 1
        rank_des = int(len(self._grades))
        result = ""
        for key, item in grades:
            result = result + item.gid + ","
            result = result + item.stname + ","
            result = result + str(int(item.kor)) + ","
            result = result + str(int(item.eng)) + ","
            result = result + str(int(item.mat)) + ","
            result = result + str(int(item.gsum)) + ","
            result = result + str(item.avg) + "\n"
            if order_key == 'rank':
                result = result.rstrip("\n")
                result = result + ","
                if order_way == 'asc':
                    result = result + str(rank_asc) + "\n"
                elif order_way == 'des':
                    result = result + str(rank_des) + "\n"
            rank_asc = rank_asc + 1
            rank_des = rank_des - 1
        return result.strip()

    def sort(self,order_key="rank", order_way="asc"):
        if order_key == "rank" and order_way =="des":
            sorted_grades = sorted(self._grades.items(),key = key_avg)
        elif order_key == "rank" and order_way == "asc":
            sorted_grades = sorted(self._grades.items(),key = key_avg,reverse=True)
        if order_key == "gid" and order_way =="asc":
            sorted_grades = sorted(self._grades.items())
        elif order_key == "gid" and order_way == "des":
            sorted_grades = sorted(self._grades.items(),reverse=True)

        result = self._make_grades_string(order_key, order_way, sorted_grades)
        return result


    def write(self,file_name,order_key="rank", order_way="asc"):
        with open(file_name, 'wt', encoding="utf-8") as fo:
            result = self.sort(order_key,order_way)
            fo.write(result)

