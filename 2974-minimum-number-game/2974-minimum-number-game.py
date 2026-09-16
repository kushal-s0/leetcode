class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=sorted(nums)
        l,r=0,1
        while l<len(nums):
            arr[l],arr[r]=arr[r],arr[l]
            l+=2
            r+=2
        return arr