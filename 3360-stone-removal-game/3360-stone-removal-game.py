class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        turn = True
        while n >= remove:
            n -= remove
            remove -= 1
            turn = not turn
        return not turn 