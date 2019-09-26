###################### 28-08-2019
########### Lucas Sampaio de Melo
####### int2roman_test.py
#### v1.0

import unittest
from source.int2roman_lucas import roman_number

class Test(unittest.TestCase):
    
    def test_formatation1(self):
        self.assertEqual(
            roman_number.keyboard2roman(12), 'XII')

    def test_out_range(self):
        self.assertEqual(
            roman_number.keyboard2roman(3000000), 'out_range')

    def test_value_wrong(self):
        self.assertEqual(
            roman_number.keyboard2roman('aaaaaaaaaa'), 'numbers_only')
    
    def test_low_value(self):
        self.assertEqual(
            roman_number.keyboard2roman(-1), 'out_range')

    def test_symbols(self):
        self.assertEqual(
            roman_number.keyboard2roman('*****%!!!!!!******'), 'numbers_only')

    def test_right(self):
        self.assertEqual(
            roman_number.keyboard2roman(2999), 'MMCMXCIX')

    def test_right(self):
        self.assertEqual(
            roman_number.keyboard2roman(1), 'I')

if __name__ == "__main__":
    unittest.main()