class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right = sum(nums)
        left = 0
        result = []
        for num in nums:
            right-=num
            result.append(abs(right-left))
            left+=num
        return result