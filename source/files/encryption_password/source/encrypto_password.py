###################### 02-09-2019
########### Lucas Sampaio de Melo
####### encrypto_password.py
#### v1.0

import hashlib
import os

class crypto_pass:
   
    @classmethod
    def hash_md5(cls, pwd):
        return hashlib.md5(str(pwd).encode('utf-8')).hexdigest()

    @classmethod
    def hash_sha256(cls, pwd):
        return hashlib.sha256(pwd.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    while True:
        try:
            # print("escolha uma forma de criptografar: M = md5 / S - sha256")
            # verifica = input("Digite sua resposta: \n")
            # if verifica == 'M' or verifica == 'm' or verifica == 'S' or verifica == 's':
            pwd = input("Digite a senha: \n")
            crypto_pass.hash_md5(pwd)
            #crypto_pass.hash_sha256(pwd)
            #     if verifica == 'M' or  verifica == 'm':
            #         crypto_pass.hash_md5(pwd)
            #     if verifica == 'S' or verifica == 's':
            #         crypto_pass.hash_sha256(pwd)
            # else:
            #     print("Digite uma resposta válida.")

        except KeyboardInterrupt:
            exit()
