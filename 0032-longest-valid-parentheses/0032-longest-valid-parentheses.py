class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxi=0
        l,r=0,0
        for char in s:
            if char=="(":
                l+=1
            else:
                r+=1
            if l==r:
                maxi=max(maxi,r*2)
            elif r>l:
                l,r=0,0
        l,r=0,0

        for char in reversed(s):
            if char=="(":
                l+=1
            else:
                r+=1
            if l==r:
                maxi=max(maxi,l*2)
            elif l>r:
                l=r=0
        return maxi