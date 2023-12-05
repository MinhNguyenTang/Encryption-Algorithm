import random
from hashlib import sha256

class Algo2:
    def __init__(self, key, message):
        self.message = self.stringToInt(message)
        self.derive_key(key)
        #self.intToString(self.message)
    
    def derive_key(self, key):
        self.key = sha256(key.encode('utf-8')).hexdigest()
    
    def xor(self):
        binary = bin(int(self.message))[2:]
        # random.seed(self.key)
        # a = bin(random.getrandbits(len(binary)))[2:]
        res = ''
        for i in range(len(binary)):
            res += str(int(binary[i]) ^ int(a[i]))
        self.message = str(int(res, 2)) 

    def stringToInt(self, text):
        res = [str(ord(i)).zfill(len(str(max([ord(c) for c in text])))) for i in text]
        return str(len(res[0])) + ''.join(res)

    def intToString(self, text):
        length = int(text[0])
        numbers = [text[i:i+length] for i in range(1, len(text), length)]
        return ''.join(chr(int(num)) for num in numbers)
    

    def encrypt_content_file(input_file, output_file):
        pass

a = Algo2('NNN', 'BBB☺♣♦☺')