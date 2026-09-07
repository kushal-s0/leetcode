class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if s[i].isalpha():
                st.append(s[i])
            else:
                st.pop()
        word = "".join(st)
        return word

        