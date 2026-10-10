class Solution:
    def canJump(self, nums: list[int]) -> bool:
        midx=0
        for i in range(len(nums)):
            if i>midx:
                return False
            midx=max(midx,i+nums[i])
        return True