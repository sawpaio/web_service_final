# coding: utf-8

###################### 27-08-2019
########### Lucas Sampaio de Melo
####### classificador_senhas_test.py
#### v1.0

import unittest
from source.classificador_senhas_lucas import Classifica

class TestClassifica(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(
            Classifica.classifica_senha(""))

    def test_only_letters(self):
        self.assertEqual(
            Classifica.classifica_senha("aaaaaaaaaaaa"), 0)
    
    def test_only_numbers(self):
        self.assertEqual(
            Classifica.classifica_senha("1111111111111111111"), 0)

    def test_only_symbols(self):
        self.assertEqual(
            Classifica.classifica_senha("****&&&&@@@!!!!*********"), 0)

    def test_password_medium_letters_and_numbers(self):
        self.assertEqual(
            Classifica.classifica_senha("aaaaaaaaaa1111111aaaaaa"), 1)

    def test_password_medium_letters_and_symbols(self):
        self.assertEqual(
            Classifica.classifica_senha("aaaaaa*****aaaaa"), 1)
    
    def test_password_medium_numbers_and_symbols(self):
        self.assertEqual(
            Classifica.classifica_senha("11111******2222$$$$$$$$####@@@@"), 1)

    def test_password_strong_w_all(self):
        self.assertEqual(
            Classifica.classifica_senha("aaaaaaaa*****8888kjnadsjdksad8282718&&&&!!!@@"), 2)