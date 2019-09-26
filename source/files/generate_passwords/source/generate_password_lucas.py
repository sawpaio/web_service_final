# coding: utf-8

###################### 26-08-2019
########### Lucas Sampaio de Melo
####### generate_password_lucas.py
#### v1.0 

import random
from random import randint

def random_pass():
    length = randint(10,30) #Gera um número aleatório entre 3 e 15 
    alpha = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz*&%#@.;/?][}{,<>$!' #declaração de caracteres possiveis
    
    password = ''
    for i in range(0,length,2):
        password += random.choice(alpha)
    return password

if __name__ == "__main__":
    random_pass()