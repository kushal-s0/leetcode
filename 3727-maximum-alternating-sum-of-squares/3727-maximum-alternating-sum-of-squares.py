class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        r=[]
        d=len(nums)//2
        for n in nums:
            r.append(n*n)
        r.sort()
        return (sum(r[d:])-sum(r[:d]))
