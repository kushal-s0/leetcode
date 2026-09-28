class Solution:
    def maxDepth(self, s: str) -> int:
        result,a=0,0
        for c in s:
            a+=(c=="(")-(c==")")
            result=max(result,a)
        return result
