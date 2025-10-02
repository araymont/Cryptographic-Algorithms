import Algorithms.ShiftCypher.ShiftCypher as ShiftCypher
import Algorithms.AffineCypher.AffineCypher as AffineCypher
import Algorithms.VigenereCypher.VigenereCypher as VigenereCypher
import Algorithms.DES.DES as DES
import Algorithms.DES


class tester():
    def __init__(self):
        self.phrase = "Hello World Hello World Hello World"

    def test_shift(self):
        cc = ShiftCypher.Shift_Cypher()
        encrypted = cc.encrypt(self.phrase,1)
        cc.decrypt(encrypted,1)

    def test_affine(self):
        cc = AffineCypher.AffineCypher(4,7)
        encrypted = cc.encrypt(self.phrase)
        cc.decrypt(encrypted)

    def test_vigenere(self):
        cc = VigenereCypher.VigenereCypher()
        encrypted = cc.encrypt(self.phrase)
        cc.decrypt(encrypted)

    def test_new(self):
        cc = DES.DES()
        encrypted = cc.encrypt(self.phrase)
        #cc.decrypt(encrypted)
        

t = tester()
t.test_new()