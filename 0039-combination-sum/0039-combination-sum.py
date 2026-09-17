class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        self.bt(0,0,[],candidates,target,result)
        return result
    def bt(self,idx,total,subset,nums,target,result):
        if total==target:
            result.append(subset.copy())
            return
        elif total>target:
            return
        if idx>=len(nums):
            return
        s=total+nums[idx]
        subset.append(nums[idx])
        self.bt(idx,s,subset,nums,target,result)
        s=total
        subset.pop()
        self.bt(idx+1,s,subset,nums,target,result)


