class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        st=[]
        result=[]
        count=0
        for ch in seq:
            if ch=="(":
                st.append("(")
                count+=1
                if count%2==0:
                    result.append(1)
                else:
                    result.append(0)
            else:
                st.pop()
                if count%2==0:
                    result.append(1)
                else:
                    result.append(0)
                count-=1
        return result