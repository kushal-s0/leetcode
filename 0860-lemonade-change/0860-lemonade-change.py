class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        n=len(bills)
        f,t=0,0
        for i in range(n):
            if bills[i]==5:
                f+=1
            elif bills[i]==10:
                if f>=1:
                    f-=1
                    t+=1
                else:
                    return False
            else:
                if f>=1 and t>=1:
                    f-=1
                    t-=1
                elif f>=3:
                    f-=3
                else:
                    return False
        return True 