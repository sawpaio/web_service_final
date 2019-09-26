# coding: utf-8

###################### 27-08-2019
########### Lucas Sampaio de Melo
####### classificador_senhas_lucas.py
#### v1.0

import string
import sys

class Classifica:
    """ Classe que classifica a força de uma senha."""

    @classmethod
    def classifica_senha(cls, pwd):
        if len(pwd) <= 7 or isinstance(pwd, int):
            return 'Senha Inválida.'

        flag = -1
        if verify_letters(pwd) == True:
            flag += 1

        if verify_num(pwd) == True:
            flag += 1

        if verify_symbols(pwd) == True:
            flag += 1
        
        if flag == -1:
            return 'Senha extremamente fraca'
        if flag == 0:
            return '0: senha fraca'
        if flag == 1:
            return '1: senha média'
        if flag == 2: 
            return '2: senha forte'

def verify_letters(pwd):
    letters = string.ascii_letters
    if any(char in letters for char in pwd): #Vefifica se tem apenas letras
        return True

def verify_num(pwd):
    if any(char.isdigit() for char in pwd): #Verifica se possui números.
        return True

def verify_symbols(pwd):
    if any([char in string.punctuation for char in pwd]): #Verifica se possui símbolos.
        return True


if __name__ == "__main__":
    while True:
        try:
            pwd = input("Digite uma senha:\n")
            Classifica.classifica_senha(pwd)
        except KeyboardInterrupt:
            sys.exit(0)
