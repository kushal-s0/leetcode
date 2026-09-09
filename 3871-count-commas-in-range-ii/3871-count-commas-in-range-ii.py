class Solution:
    def countCommas(self, n: int) -> int:
        cur=1000
        re=0
        while cur<=n:
            re+=n-cur+1
            cur*=1000
        return re

        
        