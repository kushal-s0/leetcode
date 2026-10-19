class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        r=[]
        for i in range(len(nums)):
            if nums[i]>target:
                break
            elif nums[i]==target:
                r.append(i)
        return r