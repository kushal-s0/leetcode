class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        h={}
        for n in nums:
            h[n]=h.get(n,0)+1
        return [key for key,value in h.items() if value==2]