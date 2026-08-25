class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        myset=set(nums)
        for i in range(1,1000):
            n=k*i
            if n not in myset:
                return n

        