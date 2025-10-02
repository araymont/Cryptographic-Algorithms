import Algorithms.DES.FeistalBox as DESFbox

class DES():
    def __init__(self):
        DESFbox

    def encrypt(self,phrase):
        bytedKey=map(bin,bytearray(phrase,'utf8'))
        bytedKeyArray = []
        for i in bytedKey:
            val=i.split('b')
            val=''.join(val)
            bytedKeyArray.append(val)
        fBytedKey = ''.join(bytedKeyArray)
        

    def round(self):
        pass

    def decrypt(self):
        pass