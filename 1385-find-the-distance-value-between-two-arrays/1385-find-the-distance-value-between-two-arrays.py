class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count=0
        for i in range(len(arr1)):
            t=False
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    t=True
            if t:
                continue
            count+=1
        return count


        