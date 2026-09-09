class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l=0
        r=1
        count=0
        while l<len(nums)-1:
            if r>len(nums)-1:
                l+=1
                r=l+1
                continue
            if nums[l]==nums[r]:
                count+=1
                r+=1
            else:
                r+=1
        return count