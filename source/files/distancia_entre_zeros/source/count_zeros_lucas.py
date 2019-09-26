# coding: utf-8

###################### 21-08-2019
########### Lucas Sampaio de Melo
####### count_zeros_lucas.py
#### v1.0

import unittest 
import re

class Count_zeros:

    @classmethod
    def zeros_count(cls, sequence):
        zeros_of_string = re.findall(r'0+', str(sequence))
        try:
            bigger_sequence = max(len(x) for x in zeros_of_string)
            return bigger_sequence
        
        except ValueError:
            return 0


if __name__ == "__main__":
    while True:
        sequence = input("Digite uma sequencia de números: \n")
        Count_zeros.zeros_count(sequence)
