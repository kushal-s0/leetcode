class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        self.bt(1,n,[],result,k)
        return result
    def bt(self,idx, target, subset, result, k):
        if target == 0 and len(subset)==k:
            result.append(subset.copy())
            return
        if target <0 or len(subset)>k:
            return
        for i in range(idx, 10):
            subset.append(i)
            self.bt(i + 1, target-i,subset, result,k)
            subset.pop()