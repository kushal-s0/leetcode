class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        mat=[[0]*n for _ in range(n)]
        result=[]
        self.placequeen(0,mat,result)
        return result
    def isSafe(self,mat,row,col):
        for i in range(row):
            if mat[i][col]:
                return 0
        i,j=row-1,col-1
        while i>=0 and j>=0:
            if mat[i][j]:
                return 0
            i-=1
            j-=1
        i,j=row-1,col+1
        while i>=0 and j<len(mat):
            if mat[i][j]:
                return 0
            i-=1
            j+=1
        return 1

    def placequeen(self,row,mat,result):
        n=len(mat)
        if row==n:
            a=[]
            for i in range(n):
                r=""
                for j in range(n):
                    if mat[i][j]:
                        r+="Q"
                    else:
                        r+="."
                a.append(r)
            result.append(a)
        
        for i in range(n):
            if self.isSafe(mat,row,i):
                mat[row][i]=1
                self.placequeen(row+1,mat,result)
                mat[row][i]=0
        