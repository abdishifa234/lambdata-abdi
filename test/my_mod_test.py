#wrte some code using unittest to test enlarge function

import unittest
from lambdata-abdi.my_mode.py import enlarge

class TestMymode(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(9),900)
        


    

if __name__ == '__main__':
    unittest.main() #invoking all of our class's methods
    