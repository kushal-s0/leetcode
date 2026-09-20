class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            w = 0
            for char in word:
                idx = ord(char) - ord('a')
                w += weights[idx]
            r = w % 26
            c = chr(ord('z') - r)
            result.append(c)
            
        return "".join(result)