import unittest
from name_function import get_formatted_name

class NameTestCase( unittest.TestCase):
    def test_name(self):
        formatted_name = get_formatted_name('sfs','sdv')
        self.assertEqual(formatted_name,'Sfs Sdv')
    def test_middle_name(self):
        formatted_name = get_formatted_name('sfs', 'sdv','wq')
        self.assertEqual(formatted_name, 'Sfs Wq Sdv')
if __name__=="__main__":
    unittest.main()