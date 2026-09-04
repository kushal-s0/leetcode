class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums)<=1:
            return 0
        for i in range(len(nums)):
            maxi=max(nums[:i+1])
            mini=min(nums[i:])
            if maxi-mini<=k:
                return i
        return -1
        