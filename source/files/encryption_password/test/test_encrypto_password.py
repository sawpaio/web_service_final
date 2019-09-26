###################### 02-09-2019
########### Lucas Sampaio de Melo
####### test_encrypto_password.py
#### v1.0

import unittest
from source.encrypto_password import crypto_pass

class Test(unittest.TestCase):
    def test_same_hash_sha_256(self):

        self.assertEqual(
            crypto_pass.hash_sha256('senhamuitoboa'),
             '94cb9d3dc9b7d797e77e7bca2d339cb332ec6a1d0ec41422faf2ca21a32612bd')
    
    def test_same_hash_md5(self):
        self.assertEqual(
            crypto_pass.hash_md5('senhamuitoruim'),
             '2b6b54689a02f72c4394a1faacb9c33e')

if __name__ == "__main__":
    unittest.main()