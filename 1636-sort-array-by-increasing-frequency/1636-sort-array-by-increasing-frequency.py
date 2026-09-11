class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        h = {}
        for num in nums:
            h[num]=h.get(num,0)+1
        return sorted(nums, key=lambda x: (h[x], -x))