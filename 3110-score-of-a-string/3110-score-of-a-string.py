class Solution:
    def scoreOfString(self, s: str) -> int:
        value=ord(s[0])
        total=0
        for i in range(1,len(s)):
            value=abs(value -ord(s[i]))
            total+=value
            value=ord(s[i])
        return total

        