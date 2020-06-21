import unittest
from grade_rank_system import GradeRankSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class TestGradeRankSystem(unittest.TestCase):


    def setUp(self):
        self.m_open_1 = mock_open(read_data = "1,양수열,95,92\n")
        self.m_open_2 = mock_open(read_data = "1,강호민,85,90,95\n2,김광호,80,70,60\n\n")
        self.m_open_3 = mock_open(read_data = "1,강호민,85,90,95\n2,김광호,80,70,60\n3,김민식,75,85,80\n")

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


    def test_get_gid(self):
        pass


if __name__ == "__main__":
    unittest.main()
