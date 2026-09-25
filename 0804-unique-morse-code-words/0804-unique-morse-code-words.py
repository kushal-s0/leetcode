class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        myset=set()
        for i in range(len(words)):
            s=""
            for j in range(len(words[i])):
                n=ord(words[i][j])-97
                s+=l[n]
            myset.add(s)
        return len(myset)