class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        myset=set(nums)
        i=1
        while True:
            if i*k not in myset:
                return i*k
            i+=1
            

        