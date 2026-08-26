class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        new=sorted(score,reverse=True)
        arr=[]
        for i in range(len(score)):
            for j in range(len(new)):
                if score[i]==new[j]:
                    if j==0:
                        arr.append("Gold Medal")
                    elif j==1:
                        arr.append("Silver Medal")
                    elif j==2:
                        arr.append("Bronze Medal")
                    else:
                        arr.append(str(j+1))
        return arr
        