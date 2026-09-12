class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        w2=""
        for char in word1:
            w1+=char
        for char in word2:
            w2+=char
        if w1==w2:
            return True
        return False