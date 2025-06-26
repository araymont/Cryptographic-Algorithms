import Algorithms.ShiftCypher as ShiftCypher
import Algorithms.AffineCypher as AffineCypher


class tester():
    def __init__(self):
        self.phrase = "Hello World"

    def test_shift(self):
        cc = ShiftCypher.Shift_Cypher()
        encrypted = cc.encrypt(self.phrase,1)
        cc.decrypt(encrypted,1)

    def test_new(self):
        cc = AffineCypher.AffineCypher(3,15)
        encrypted = cc.encrypt(self.phrase)
        

t = tester()
t.test_new()