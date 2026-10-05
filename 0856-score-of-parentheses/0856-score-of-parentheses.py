class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[]
        count=0
        for ch in s:
            if ch=="(":
                st.append(count)
                count=0
            else:
                count=st.pop()+max(count*2,1)

        return count