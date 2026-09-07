class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
        return result