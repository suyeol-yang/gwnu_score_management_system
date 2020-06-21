import unittest
from grade_rank_system import GradeRankSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class TestGradeRankSystem(unittest.TestCase):


    def setUp(self):
        self.m_open_1 = mock_open(read_data = "1,양수열,95,92,88\n")
        self.m_open_2 = mock_open(read_data = "1,양수열,95,92,88\n2,이승수,80,70,60\n\n")

        self.m_write_open_1 = mock_open()
        self.m_w = mock_open().return_value
        self.m_write_open_1.side_effect = [self.m_open_2.return_value,self.m_w]


    def test_constructor(self):
        tgrs = GradeRankSystem()
        self.assertIsNotNone(tgrs)

    def test_read_1(self):

        with patch('grade_rank_system.open',self.m_open_1):
            tgrs = GradeRankSystem()
            self.assertEqual(1,tgrs.read('grade_data.csv'))

        self.m_open_1.assert_called_with('grade_data.csv','rt',encoding="utf-8")

    def test_read_2(self):

        with patch('grade_rank_system.open',self.m_open_2):
            tgrs = GradeRankSystem()
            self.assertEqual(2,tgrs.read('grade_data1.csv'))



    def test_sort_1(self):
        with patch('grade_rank_system.open',self.m_open_1):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')

        result = tgrs.sort(order_key = "gid")
        self.assertEqual('1,양수열,95,92,88,275,91.7',result)

    def test_sort_2(self):
        with patch('grade_rank_system.open',self.m_open_2):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')

        result = tgrs.sort(order_key = "gid")
        self.assertEqual('1,양수열,95,92,88,275,91.7\n2,이승수,80,70,60,210,70.0',result)

    def test_sort_3(self):
        with patch('grade_rank_system.open',self.m_open_2):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')

        result = tgrs.sort(order_key = "gid",order_way="des")
        self.assertEqual('2,이승수,80,70,60,210,70.0\n1,양수열,95,92,88,275,91.7',result)


    def test_sort_4(self):
        with patch('grade_rank_system.open',self.m_open_2):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')

        result = tgrs.sort()
        self.assertEqual('1,양수열,95,92,88,275,91.7,1\n2,이승수,80,70,60,210,70.0,2',result)

    def test_sort_5(self):
        with patch('grade_rank_system.open',self.m_open_2):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')

        result = tgrs.sort(order_way="des")
        self.assertEqual('2,이승수,80,70,60,210,70.0,2\n1,양수열,95,92,88,275,91.7,1',result)


    def test_write_1(self):
        with patch('grade_rank_system.open',self.m_write_open_1):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')
            tgrs.write('result.csv')

        self.m_w.write.assert_called_with('1,양수열,95,92,88,275,91.7,1\n2,이승수,80,70,60,210,70.0,2')

    def test_write_2(self):
        with patch('grade_rank_system.open',self.m_write_open_1):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')
            tgrs.write('result.csv','rank','des')

        self.m_w.write.assert_called_with('2,이승수,80,70,60,210,70.0,2\n1,양수열,95,92,88,275,91.7,1')

    def test_write_3(self):
        with patch('grade_rank_system.open',self.m_write_open_1):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')
            tgrs.write('result.csv','gid','asc')

        self.m_w.write.assert_called_with('1,양수열,95,92,88,275,91.7\n2,이승수,80,70,60,210,70.0')

    def test_write_4(self):
        with patch('grade_rank_system.open',self.m_write_open_1):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')
            tgrs.write('result.csv','gid','des')

        self.m_w.write.assert_called_with('2,이승수,80,70,60,210,70.0\n1,양수열,95,92,88,275,91.7')

if __name__ == "__main__":
    unittest.main()
