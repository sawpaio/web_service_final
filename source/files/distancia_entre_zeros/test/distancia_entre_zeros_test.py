# coding: utf-8

###################### 21-08-2019
########### Lucas Sampaio de Melo
####### count_zeros_lucas.py
#### v1.0

import unittest
from source.count_zeros_lucas import Count_zeros

class TestContaZeros(unittest.TestCase):

    def test_count_zeros(self):
        self.assertEqual(
            Count_zeros.zeros_count(
                '000000000000000'), 15)

    def test_count_zeros_with_char(self):
        self.assertEqual(
            Count_zeros.zeros_count(
                'dnasijdnaskj00dha'), 2)
    
    def test_count_zeros_multiple(self):
        self.assertEqual(
            Count_zeros.zeros_count(
                '919001220000012001200000011'), 6)

    def test_count_zeros_with_symbols(self):
        self.assertEqual(
            Count_zeros.zeros_count(
                '*******00*****&&&&$$$$$00######00'), 2)

    def test_count_zeros_without_zeros(self):
        self.assertEqual(
            Count_zeros.zeros_count(
                '11111111111'), 0)

    def test_count_zeros_empty(self):
        self.assertEqual(
            Count_zeros.zeros_count(
                ' '), 0)
    
    def test_count_zeros_random(self):
        self.assertEqual(
            Count_zeros.zeros_count(
            'DIANDIJASNDIASNDASI DJASNDJASDNSANDASKJNDASK jidandasnsann'), 0)

    def test_count_zeros_w_spaces(self):
        self.assertEqual(
            Count_zeros.zeros_count(
                '00 00 00 00 00 000000 00'), 6)
    

if __name__ == '__main__':
    unittest.main()