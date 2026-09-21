class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=str(n)
        c=0
        for i in range(len(s)):
            c+=int(s[i])
        return c