class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}
        for i in s:
            h[i]=h.get(i,0)+1
        for idx,i in enumerate(s):
            if h[i]==1:
                return idx
        return -1
        
            
        