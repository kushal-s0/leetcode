class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini = float('inf')
        
        for num in nums:
            summ = 0
            while num > 0:
                num, digit = divmod(num, 10)
                summ += digit
            if summ < mini:
                mini = summ
                
        return mini