import random

class AffineCypher():
    def __init__(self,b,a=0):
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        if(a == 0):
            self.k = self.find_a(a),b
        else:
            self.k = a,b
        self.has_encrypted = False
        self.a_options = [1,2,3,5,7,9,11,15,17,19,21,23,25]

    def find_a(self,a):
        loc = random.randint(0,13)
        return self.a_options[loc]

    

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
        ind = self.a_options.index(self.k[0])
        #print(ind)
        inverse_list = [1,'',9,'',21,'',15,'',3,'',19,'','','',7,'',23,'',11,'',5,'',17,'',25]
        return inverse_list[self.k[0]-1]
        val = 0
        for i in range(1,26):
            for j in range(1,200):
                res = (i*j) % 26
                if(res == 1):
                    print("Miltiplicitive Inverse of ", i, "is ",j)
                    break

    def decrypt(self,phrase):
        new_phrase = []
        inv = self.find_inverse()
        #print(inv,"\n\n")
        for i in range(0,len(phrase)):
            if(phrase[i] == ' '):
                new_phrase.append(' ')
            elif(phrase[i] == phrase[i].lower()):
                ind = self.alphabet.index(phrase[i])
                new_ind = ((ind - (self.k[1])) * inv) %26
                new_phrase.append(self.alphabet[new_ind])
            else:
                ind = self.alphabet.index(phrase[i].lower())
                new_ind = ((ind - (self.k[1])) * inv) %26
                new_phrase.append(self.alphabet[new_ind].upper())
        print("".join(new_phrase))