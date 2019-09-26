###################### 16-08-2019
########### Lucas Sampaio de Melo
####### int2roman_lucas.py
#### v1.1

import os

dictionary = [(1000, 'M'), (900, 'CM'), (500, 'D'),
              (400, 'CD'), (100, 'C'), (90, 'XC'),
              (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
              (5, 'V'), (4, 'IV'), (1, 'I')]

class roman_number:

    @classmethod
    def keyboard2roman(cls, value):
        try:
            valor = int(value)
            if valor > 3000 or valor <= 0:
                return 'out_range'
            else:
                output = ''

                while valor > 0:
                    for integer, roman in dictionary:
                        while valor >= integer:
                            output += roman
                            valor -= integer
                return output
        except ValueError:
            return 'numbers_only'

if __name__ == "__main__":
    while True:
        try:
            value = input("Digite um número para ser convertido.\n")
            roman_number.keyboard2roman(value)
        except KeyboardInterrupt:
            exit(0)
