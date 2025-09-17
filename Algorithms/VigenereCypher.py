


class VigenereCypher():
    def __init__(self,key = 'password'):
        self.key = []
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in key:
            val = self.alphabet.index(i)
            self.key.append(val)

    def encrypt(self,phrase):
        pass

    def decypt(self,phrase):
        pass

