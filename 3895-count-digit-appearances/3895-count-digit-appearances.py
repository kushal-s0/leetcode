class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        d=str(digit)
        count=0
        for i in range(len(nums)):
            n=str(nums[i])
            for j in range(len(n)):
                if n[j]==d:
                    count+=1
        return count