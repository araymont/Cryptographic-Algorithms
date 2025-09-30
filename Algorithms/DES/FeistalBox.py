import DesKey as DesKey


class FeistalBox():
    def __init__(self):
        key = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        self.keyGenerator = DesKey(key)

    def getResult(self,halfBlock):
        halfBlockExpanded = self.expandInput(halfBlock)
        subkey = self.keyGenerator.getKey()
        combined = self.xorFunction(halfBlockExpanded,subkey)
        substituted = self.sBoxSubstitution(combined)
        return self.permutation(substituted)


    def expandInput(self,input):
        newInput=[
            input[31],input[0],input[1],input[2],input[3],input[4],input[3],input[4],
            input[5],input[6],input[7],input[8],input[7],input[8],input[9],input[10],
            input[11],input[12],input[11],input[12],input[13],input[14],input[15],input[16],
            input[15],input[16],input[17],input[18],input[19],input[20],input[19],input[20],
            input[21],input[22],input[23],input[24],input[23],input[24],input[25],input[26],
            input[27],input[28],input[27],input[28],input[29],input[30],input[31],input[0]
        ]
        return newInput

    def xor(self,x,y):
        if(x == 1):
            if(y==1):
                return 0
            else:
                return 1
        else:
            if(y==1):
                return 1
            else:
                return 0

    def xorFunction(self,expandedBlock,subkey):
        preSBox = []
        count=0
        for i in expandedBlock:
            preSBox.append(self.xor(i,subkey[count]))
            count+=1
        return preSBox

    def sBoxSubstitution(self,input):
        new=[]
        for i in range(0,int(len(input)/6)):
            boxIn1 = (input[i*6],input[((i+1)*6)-1])
            boxIn2 = input[(i*6)+1:((i+1)*6)-1]
            new.append(self.sBox(boxIn1,boxIn2))
        print(new)

    def binaryToDecimal(self,input):
        val=0
        for i in range(0,len(input)):
            if(input[i]=='1'):
                val+=pow(2,(i+1))
        return val

    def sBox(self,boxIn1,boxIn2):
        sBoxDict={
            (0,0):['0010','1100','0100','0001','0111','1010','1011','0110','1000','0101','0011','1111','1101','0000','1110','1001'],
            (0,1):['1110','1011','0010','1100','0100','0111','1101','0001','0101','0000','1111','1010','0011','1001','1000','0110'],
            (1,0):['0100','0010','0001','1011','1010','1101','0111','1000','1111','1001','1100','0101','0110','0011','0000','1110'],
            (1,1):['1011','1000','1100','0111','0001','1110','0010','1101','0110','1111','0000','1001','1010','0100','0101','0011']
        }
        sBoxValue=sBoxDict[boxIn1]
        return sBoxValue[self.binaryToDecimal(boxIn2)]

    def permutation(self,substitutedResult):
        indexs=[16,7,20,21,29,12,28,17,
                1,15,23,26,5,18,31,10,
                2,8,24,14,32,27,3,9,
                19,13,30,6,22,11,4,25]
        newResult = []
        for i in indexs:
            newResult.append(substitutedResult[i-1])
        return newResult