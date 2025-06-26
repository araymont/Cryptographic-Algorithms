import random

class AffineCypher():
    def __init__(self,b,a=0):
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        if(a == 0):
            self.k = self.find_a(a),b
        else:
            self.k = a,b
        self.has_encrypted = False

    def find_a(self,a):
        options=[1,2,3,5,7,9,11,15,17,19,21,23,25]
        loc = random.randint(0,13)
        return options[loc]

    

    def encrypt(self,phrase):
        self.has_encrypted = True
        new_phrase = []
        for i in range(0,len(phrase)):
            if(phrase[i] == ' '):
                new_phrase.append(' ')
            else:
                if(phrase[i] == phrase[i].lower()):
                    index = self.alphabet.index(phrase[i])
                    new_index = ((index * self.k[0]) + self.k[1]) % 26
                    new_phrase.append(self.alphabet[new_index])
                else:
                    index = self.alphabet.index(phrase[i].lower())
                    new_index = ((index * self.k[0]) + self.k[1]) % 26
                    new_phrase.append(self.alphabet[new_index].upper())
        print("".join(new_phrase))
        return new_phrase

    def find_inverse(self):
        pass

    def decrypt(self,phrase):
        pass