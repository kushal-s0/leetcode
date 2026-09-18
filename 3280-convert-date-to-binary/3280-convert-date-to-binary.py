class Solution:
    def convertDateToBinary(self, date: str) -> str:
        r=""
        temp=""
        for i in range(len(date)):
            if date[i]=="-":
                r+=bin(int(temp))[2:]
                r+="-"
                temp=""
            elif i==len(date)-1:
                temp+=date[i]
                r+=bin(int(temp))[2:]
            else:
                temp+=date[i]
        return r