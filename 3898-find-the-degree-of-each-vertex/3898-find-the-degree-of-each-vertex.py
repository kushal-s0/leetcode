class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        # result=[]
        # for i in range(len(matrix)):
        #     count=0
        #     for j in range(len(matrix[0])):
        #         count+=matrix[i][j]
        #     result.append(count)
        # return result

        return [sum(m) for m in matrix]

        