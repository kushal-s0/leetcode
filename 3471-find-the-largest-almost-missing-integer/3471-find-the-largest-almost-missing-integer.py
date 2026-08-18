class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d={}
        ans=-1
        if k==len(nums):
            return max(nums)
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        if k==1:
            ans=-1
            for num,idx in d.items():
                if idx==1 and num>ans:
                    ans=num
            return ans
        f=nums[0]
        l=nums[-1]
        if d[f]==1:
            if f>ans:
                ans=f
        if d[l]==1:
            if l>ans:
                ans=l
        return ans
        
            
            
        