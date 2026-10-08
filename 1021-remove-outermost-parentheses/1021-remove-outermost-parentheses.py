class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result=[]
        count=0
        for ch in s:
            if ch=="(" and count>0:
                result.append(ch)
            if ch==")" and count>1:
                result.append(ch)
            if ch=="(":
                count+=1
            else:
                count-=1
        return "".join(result)