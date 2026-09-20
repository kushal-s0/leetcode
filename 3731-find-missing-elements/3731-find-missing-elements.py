class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=set(nums)
        mini=min(s)
        maxi=max(s)
        r=[]
        for i in range(mini,maxi):
            if i not in s:
                r.append(i)
        return r