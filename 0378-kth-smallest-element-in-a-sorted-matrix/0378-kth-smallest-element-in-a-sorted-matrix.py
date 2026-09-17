class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        if len(matrix)<2:
            return matrix[k-1][k-1]
        result=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                result.append(matrix[i][j])
        result.sort()
        return result[k-1]