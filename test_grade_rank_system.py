import unittest
from grade_rank_system import GradeRankSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class TestGradeRankSystem(unittest.TestCase):


    def setUp(self):
        self.m_open_1 = mock_open(read_data = "1,양수열,95,92,88\n")
        self.m_open_2 = mock_open(read_data = "1,양수열,95,92,88\n2,이승수,80,70,60\n\n")
        self.m_open_3 = mock_open(read_data = "1,양수열,95,92,88\n2,이승수,80,70,60\n3,장규범,75,85,80\n")

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


    def test_read_3(self):

        with patch('grade_rank_system.open',self.m_open_3):
            tgrs = GradeRankSystem()
            self.assertEqual(3,tgrs.read('grade_data1.csv'))

    def test_sort_by_gid_1(self):
        with patch('grade_rank_system.open',self.m_open_1):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')

        result = tgrs.sort_by_gid(order="asc")
        self.assertEqual('1,양수열,95,92,88,275,91.7',result)

    def test_sort_by_gid_2(self):
        with patch('grade_rank_system.open',self.m_open_2):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')

        result = tgrs.sort_by_gid(order="asc")
        self.assertEqual('1,양수열,95,92,88,275,91.7\n2,이승수,80,70,60,210,70.0',result)

    def test_sort_by_gid_3(self):
        with patch('grade_rank_system.open',self.m_open_2):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')

        result = tgrs.sort_by_gid(order="des")
        self.assertEqual('2,이승수,80,70,60,210,70.0\n1,양수열,95,92,88,275,91.7',result)


    def test_sort_by_rank_1(self):
        with patch('grade_rank_system.open',self.m_open_2):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')

        result = tgrs.sort_by_rank(order="asc")
        self.assertEqual('2,이승수,80,70,60,210,70.0\n1,양수열,95,92,88,275,91.7',result)

    def test_sort_by_rank_2(self):
        with patch('grade_rank_system.open',self.m_open_2):
            tgrs = GradeRankSystem()
            tgrs.read('grade.csv')

        result = tgrs.sort_by_rank(order="des")
        self.assertEqual('1,양수열,95,92,88,275,91.7\n2,이승수,80,70,60,210,70.0',result)


if __name__ == "__main__":
    unittest.main()
