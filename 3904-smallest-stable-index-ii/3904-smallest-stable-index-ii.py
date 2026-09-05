class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        smax = [0] * n
        smax[0] = nums[0]
        lmin = [0] * n
        lmin[-1] = nums[-1]
        for i in range(1, n):
            smax[i] = max(smax[i-1], nums[i])
        for i in range(n-2, -1, -1):
            lmin[i] = min(lmin[i+1], nums[i])
        for i in range(n):
            if smax[i] - lmin[i] <= k:
                return i
        return -1