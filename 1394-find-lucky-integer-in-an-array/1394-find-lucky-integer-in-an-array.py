class Solution:
    def findLucky(self, arr: list[int]) -> int:
        h={}
        for n in arr:
            h[n]=h.get(n,0)+1
        m = -1
        for num, freq in h.items():
            if num == freq:
                m = max(m, num)
        return m
        