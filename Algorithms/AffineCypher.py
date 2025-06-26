import random

class AffineCypher():
    def __init__(self,b,a=0):
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',
                         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        if(a == 0):
            k = self.find_inverse(a),b
        else:
            k = a,b

    def find_inverse(self,a):
        options=[1,2,3,5,7,9,11,15,17,19,21,23,25]
        loc = random.randint(0,13)
        return options[loc]


    def encrypt(self,phrase):
        for i in range(0,len(phrase)):
            pass

    def decrypt(self,phrase):
        pass