class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        if n<=k:
            return sum(cardPoints)
        w=n-k
        curr=sum(cardPoints[:w])
        total=sum(cardPoints)
        maxi=total-curr
        for i in range(w,n):
            curr+=cardPoints[i] - cardPoints[i - w]
            maxi=max(maxi,total-curr)
        return maxi