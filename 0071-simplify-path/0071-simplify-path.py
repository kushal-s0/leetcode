class Solution:
    def simplifyPath(self, path: str) -> str:
        d=path.split("/")
        st=[]

        for char in d:
            if char==".." and st:
                st.pop()
            elif char=="." or char==".." or char=="":
                continue
            else:
                st.append(char)
        r=""
        for c in st:
            r+="/"+c
        return "/" if r=="" else r 
        