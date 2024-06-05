import unittest
from ripasso.ripasso2 import Calc
class TestCalculetion(unittest.TestCase):
    def setUp(self):
        self.calculetion=Calc(8,2)
        
    def test_sum(self):
        self.assertEqual(self.calculetion.get_sum(),10,'The sum is wrong')
        
if __name__ =="__main__":
    unittest.main()