class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        d=[]
        non=[]
        for i in range(n+1):
            if i%m==0:
                non.append(i)
            else:
                d.append(i)
        return (sum(d)-sum(non))