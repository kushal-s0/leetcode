class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result =[]
        def bt(f):
            if f ==len(nums):
                result.append(nums[:])
                return 
            for i in range(f,len(nums)):
                nums[f],nums[i]=nums[i],nums[f]
                bt(f+1)
                nums[f],nums[i]=nums[i],nums[f]
        bt(0)
        unique = set(tuple(x) for x in result)
        return [list(x) for x in unique]
        