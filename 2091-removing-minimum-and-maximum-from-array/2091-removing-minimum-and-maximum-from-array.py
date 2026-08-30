class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini=float('inf')
        maxi=float('-inf')
        mini_idx=0
        max_idx=0
        for i in range(len(nums)):
            if nums[i]>maxi:
                maxi=nums[i]
                max_idx=i
            if nums[i]<mini:
                mini=nums[i]
                mini_idx=i
        start = min(mini_idx, max_idx)
        end = max(mini_idx, max_idx)
        return min(end+1,len(nums)-start,(start+1)+(len(nums)-end))
            

        