

class DesKey():
    def __init__(self,key):
        self.key = key
        self.calls=0
        self.leftKey=[]
        self.rightKey=[]

    # PC-1
    def inititalPermutation(self):
        parityBits=[self.key[7],self.key[15],self.key[23],self.key[31],self.key[39],self.key[47],self.key[55],self.key[63]]
        left = [57,49,41,33,25,17,9,
                1,58,50,42,34,26,18,
                10,2,59,51,43,35,27,
                19,11,3,60,52,44,36]
        right = [63,55,47,39,31,23,15,
                 7,62,54,46,38,30,22,
                 14,6,61,53,45,37,29,
                 21,13,5,28,20,12,4]
        leftList=[]
        rightList=[]
        for i in left:
            leftList.append(self.key[i-1])
        for i in right:
            rightList.append(self.key[i-1])
        self.leftKey=leftList
        self.rightKey=rightList

    def rotateLeft(self,list):
        val=list.pop(0)
        list.append(val)
        return list
    
    def permutedChioce2(self):
        self.leftKey = self.rotateLeft(self.leftKey)
        self.rightKey = self.rotateLeft(self.rightKey)
        list = self.leftKey + self.rightKey
        indexs=[14,17,11,24,1,5,
                3,28,15,6,21,10,
                23,19,12,4,26,8,
                16,7,27,20,13,2,
                41,52,31,38,47,55,
                30,40,51,45,33,48,
                44,49,39,56,34,53,
                46,42,50,36,29,32]
        permedList=[]
        for i in indexs:
            permedList.append(list[i-1])
        return permedList

    def calcKey(self):
        if(self.calls == 0):
            self.inititalPermutation()
            self.calls+=1
        return self.permutedChioce2()


    def getKey(self):
        return self.calcKey()




test = DesKey([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1])
val = test.getKey()
print(val,len(val))