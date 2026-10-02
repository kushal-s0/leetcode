class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        a,b=0,0
        for num in nums:
            xor^=num
        d=xor & -xor
        for num in nums:
            if num & d:
                a^=num
            else:
                b^=num
        return [a,b]

        