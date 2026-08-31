class Solution:
    def maxDistinct(self, s: str) -> int:
        h={}
        for char in s:
            h[char]=h.get(char,0)+1
        return len(h)
        