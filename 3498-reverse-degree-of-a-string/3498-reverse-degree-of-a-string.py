class Solution:
    def reverseDegree(self, s: str) -> int:
        count=0
        for i,c in enumerate(s):
            r=26 - (ord(c) - ord('a'))
            count+=(r*(i+1))
        return count