class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        sub=[]
        def bt(a):
            if len(sub)==k:
                result.append(sub[:])
                return
            for num in range(a,n+1):
                sub.append(num)
                bt(num+1)
                sub.pop()
        bt(1)
        return result