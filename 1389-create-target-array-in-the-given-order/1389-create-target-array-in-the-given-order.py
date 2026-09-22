class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        arr=[]
        for n,i in zip(nums,index):
            arr.insert(i,n)
        return arr
