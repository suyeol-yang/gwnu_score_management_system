import unittest
from grade import Grade

class TestGrade(unittest.TestCase):

    def setUp(self):
        self.my_grade1 = Grade("1,강호민,85,90,95")
        self.my_grade2 = Grade("2,김광호,80,70,60")


    def tearDown(self):
        del self.my_grade1
        del self.my_grade2


    def test_constructor(self):
        self.assertIsNotNone(self.my_grade1)
        self.assertIsNotNone(self.my_grade2)

    def test_gid_1(self):
        self.assertEqual("1",self.my_grade1.gid)

    def test_gid_2(self):
        self.assertEqual("2",self.my_grade2.gid)

    def test_stname(self):
        self.assertEqual("강호민",self.my_grade1.stname)
        self.assertEqual("김광호",self.my_grade2.stname)

    def test_kor(self):
        self.assertEqual(85,self.my_grade1.kor)
        self.assertEqual(80,self.my_grade2.kor)

    def test_eng(self):
        self.assertEqual(90,self.my_grade1.eng)
        self.assertEqual(70,self.my_grade2.eng)

    def test_mat(self):
        self.assertEqual(95,self.my_grade1.mat)
        self.assertEqual(60,self.my_grade2.mat)

    def test_gsum(self):
        self.assertEqual(270,self.my_grade1.gsum)
        self.assertEqual(210,self.my_grade2.gsum)

    def test_avg(self):
        self.assertEqual(90,self.my_grade1.avg)
        self.assertEqual(70,self.my_grade2.avg)

if __name__ == "__main__":
    unittest.main()