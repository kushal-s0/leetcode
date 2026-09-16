class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        arr=[]
        nums.sort()
        l,r=0,len(nums)-1
        while l<r:
            arr.append((nums[l]+nums[r])/2)
            l+=1
            r-=1
        arr.sort()
        return arr[0]