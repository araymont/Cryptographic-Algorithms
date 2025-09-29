
class FeistalBox():
    def __init__(self):
        pass

    def getResult(self,halfBlock):
        pass

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

    def sBoxSubstitution(self,input):
        pass