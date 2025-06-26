import Algorithms.ShiftCypher as ShiftCypher


class tester():
    def __init__(self):
        self.phrase = "Hello World!"

    def test_new(self):
        cc = ShiftCypher.Shift_Cypher()
        encrypted = cc.encrypt(self.phrase,1)
        cc.decrypt(encrypted,1)
        

t = tester()
t.test_new()