class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # maxi=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         n=(nums[i]-1)*(nums[j]-1)
        #         if n>maxi:
        #             maxi=n
        # return maxi

        a=max(nums)
        nums.remove(a)
        b=max(nums)
        return (a-1)*(b-1)