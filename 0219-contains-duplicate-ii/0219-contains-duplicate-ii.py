class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h=set()
        for i, num in enumerate(nums):
            if i>k:
                h.remove(nums[i-k-1])
            if num in h:
                return True
            h.add(num)
        return False

        