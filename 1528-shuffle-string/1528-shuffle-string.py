class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        l=[""]*len(s)
        a=0
        b=0
        while a<len(s):
            l[indices[b]]=s[a]
            a+=1
            b+=1
        return "".join(l)