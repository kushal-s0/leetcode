class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        my_set=set(nums)
        for num in range(len(nums)+1):
            if num in my_set:
                continue
            else:
                return num                

        