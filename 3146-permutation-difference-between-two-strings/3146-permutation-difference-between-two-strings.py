class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        h={}
        total=0
        for i,char in enumerate(s):
            h[char]=i
        for i,char in enumerate(t):
            total+=abs(i-h[char])
        return total