


class VigenereCypher():
    def __init__(self,key = 'password'):
        self.key = []
        self.keyphrase=key
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in key:
            val = self.alphabet.index(i)
            self.key.append(val)
        #print(self.key)

    def encrypt(self,phrase):
        fin = []
        phrase = phrase.lower()
        loc=[]
        count=0
        for i in phrase:
            if(i not in self.alphabet):
                loc.append(' ')
                fin.append(' ')
            else:
                val = (self.alphabet.index(i) + self.key[count % (len(self.key)-1)]) % 26
                loc.append(val)
                fin.append(self.alphabet[val])
                count+=1
        print(''.join(fin))
        return (''.join(fin))
        

    def decrypt(self,phrase):
        fin = []
        phrase = phrase.lower()
        loc=[]
        count=0
        for i in phrase:
            if(i not in self.alphabet):
                loc.append(' ')
                fin.append(' ')
            else:
                val = (self.alphabet.index(i) - self.key[count % (len(self.key)-1)]) % 26
                loc.append(val)
                fin.append(self.alphabet[val])
                count+=1
        print(''.join(fin))

