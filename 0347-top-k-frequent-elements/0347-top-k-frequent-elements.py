class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for num in nums:
            h[num]=h.get(num,0)+1
        values=sorted(h,key=h.get,reverse=True)
        return values[:k]
        