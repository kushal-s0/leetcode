class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        idx = word.index(ch)
        st = list(word[:idx+1])
        r = ""
        while st:
            r+= st.pop()
        return r + word[idx+1:]
        