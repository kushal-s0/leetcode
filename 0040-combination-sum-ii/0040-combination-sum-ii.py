class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        self.bt(0, target, [], candidates, result)
        return result

    def bt(self, idx, total, subset, nums, result):
        if total == 0:
            result.append(subset.copy())
            return
        elif total < 0:
            return
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.bt(i + 1, total - nums[i], subset, nums, result)
            subset.pop()