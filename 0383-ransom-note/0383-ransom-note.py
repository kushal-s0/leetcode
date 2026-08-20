class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h={}
        for c in magazine:
            h[c]=h.get(c,0)+1
        for c in ransomNote:
            if c not in h or h[c]<=0:
                return False
            h[c]-=1
        return True    
        