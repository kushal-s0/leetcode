class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        a,b=source[0],source[1]
        x,y=target[0],target[1]
        if(a+b)%2 != (x+y)%2:
            return -1
        elif abs(a-x)==abs(b-y):
            return 1
        else:
            return 2

