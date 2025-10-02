#import FeistalBox as DESFbox

class DES():
    def __init__(self):
        #box = DESFbox()
        pass

    def encrypt(self,phrase):
        bytedKey=map(bin,bytearray(phrase,'utf8'))
        bytedKeyArray = []
        for i in bytedKey:
            val=i.split('b')
            val=''.join(val)
            bytedKeyArray.append(val)
        fBytedKey = ''.join(bytedKeyArray)
        length = len(fBytedKey)/64
        length = int(length)
        byteArray=[]
        for i in range(0,length):
            byteArray.append(fBytedKey[i*64:(i+1)*64])
        byteArray.append(fBytedKey[(length)*64:-1])
        last = byteArray[-1]
        while(len(last) < 64):
            last += '0'
        byteArray[-1] = last
        for i in byteArray:
            print(len(i),i)
        

    def encryptRound(self):
        pass

    def round(self):
        pass

    def decrypt(self):
        pass