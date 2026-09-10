class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total=0
        product=1
        for char in str(n):
            total+=int(char)
            product*=int(char)
        return product-total 
        