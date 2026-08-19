class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        t=1<<n
        result=[]
        for num in range(t):
            lst=[]
            for i in range(n):
                if num &(1<<i)!=0:
                    lst.append(nums[i])
            result.append(lst)
        return result

        