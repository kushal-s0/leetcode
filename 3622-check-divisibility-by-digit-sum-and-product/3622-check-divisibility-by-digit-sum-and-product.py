class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total=0
        product=1
        for num in str(n):
            total+=int(num)
            product*=int(num)
        if n%(total+product)==0 :
            return True
        else:
            return False
        