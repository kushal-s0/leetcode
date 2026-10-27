class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        r=[["#"] *n for _ in range(m)]
        for j in range(n):
            r[0][j]="."
        for i in range(m):
            r[i][n-1]="."
        return [''.join(row) for row in r]