class Solution:
    def pivotInteger(self, n: int) -> int:
        a=[]
        for i in range(1,n+1):
            a.append(i)
        for i in range(1,n+1):
            l=sum(a[:i])
            r=sum(a[i-1:])
            if l==r:
                return i
        return -1