class Solution:
    def sumGame(self, num: str) -> bool:
        sumfirst=0
        sumsecond=0
        q_first = 0
        q_second = 0
        n=len(num)//2
        for i in range(n):
            if num[i]=="?":
                q_first+=1
            else:
                sumfirst+=int(num[i])
        for j in range(n,len(num)):
            if num[j] == "?":
                q_second += 1
            else:
                sumsecond += int(num[j])
        if (sumfirst - sumsecond) * 2 == (q_second - q_first) * 9:
            return False
        return True    
                 
        