class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        n=[]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                n.append(nums[i])
        return n