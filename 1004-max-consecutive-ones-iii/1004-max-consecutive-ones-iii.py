class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l,r,z=0,0,0
        maxi=0
        while r<len(nums):
            if nums[r]==0:
                z+=1
            if z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            if z<=k:
                maxi=max(maxi,r-l+1)
            r+=1
        return maxi



        # maxi=0
        # for i in range(len(nums)):
        #     z=0
        #     for j in range(i,len(nums)):
        #         if nums[j]==0:
        #             z+=1
        #         if z>k:
        #             break
        #         maxi=max(maxi,j-i+1)
        # return maxi


