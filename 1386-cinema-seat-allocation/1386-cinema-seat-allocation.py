class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        maps={}
        ans=0
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                if row not in maps:
                    maps[row] = set()
                maps[row].add(col)
        ans=(n-len(maps))*2
        for key,value in maps.items():
            left=True
            right=True
            middle=True
            for item in value:
                if 2<=item<=5:
                    left=False
                if 6<=item<=9:
                    right=False
                if 4<=item<=7:
                    middle=False
            if left and right:
                ans+=2
            else:
                if left or right or middle:
                    ans+=1
        return ans




        
        
