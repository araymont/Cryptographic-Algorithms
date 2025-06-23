
class Ceaser_Cypher():
    def __init__(self):
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',
                         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.alphabet_advanced = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ',
                                  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                                  '!','@','.',',','','-','_','(',')','*','%','&','?','/']
        self.special = ['!','@','.',',','','-','_','(',')','*','%','&','?','/']
        self.shift=0
    
    def encrypt(self,phrase, shift, alphabet = None):
        if(alphabet == None):
            breaks = False
            for l in self.special:
                if(breaks):
                    break
                if(l in phrase):
                    alphabet = self.alphabet_advanced
                    breaks = True
            if(not breaks):
                alphabet = self.alphabet
        new_phrase = []
        for i in range(0,len(phrase)):
            loc = alphabet.index(phrase[i])
            print(loc,(loc+shift),(loc+shift)%26)
            loc = (loc + shift) % len(self.alphabet)
            new_phrase.append(alphabet[loc])
        print("The encrypted phrase is: ",end="")
        print("".join(new_phrase))