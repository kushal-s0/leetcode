class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        r = 0
        n = len(intervals)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if max(intervals[i][0], intervals[j][0]) <= min(intervals[i][1], intervals[j][1]):
                    r += 1   
        return r
