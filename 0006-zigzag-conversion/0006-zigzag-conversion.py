class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        i,d=0,1
        row=[""]*numRows
        for char in s:
            row[i]+=char
            if i==0:
                d=1
            elif i==numRows-1:
                d=-1
            i+=d
            
        return "".join(row)
        
        