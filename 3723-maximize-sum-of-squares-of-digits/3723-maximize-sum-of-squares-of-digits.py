class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum<1 or sum>9*num:
            return ""
        a=sum//9
        b=sum%9
        ans=["9"]*a
        if b>0:
            ans.append(str(b))
        zero= num-len(ans)
        ans.extend(["0"]*zero)
        return "".join(ans)