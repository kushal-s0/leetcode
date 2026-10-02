class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        h={}
        l,r=0,0
        maxi=0
        while r<len(fruits):
            h[fruits[r]]=h.get(fruits[r],0)+1
            if len(h)>2:
                h[fruits[l]]-=1
                if h[fruits[l]]==0:
                    del h[fruits[l]] 
                l+=1
            if len(h)<=2:
                maxi=max(maxi,r-l+1)
            r+=1
        return maxi