class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        h={}
        for n in nums:
            h[n]=h.get(n,0)+1
        return sum(key for key, value in h.items() if value == 1)