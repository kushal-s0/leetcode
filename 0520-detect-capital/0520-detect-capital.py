class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first=False
        count=0
        for i in range(len(word)):
            if i==0 and word[i].isupper():
                first=True
            elif word[i].islower():
                count+=1
            else:
                continue
        if (count==len(word)-1 and first) or count==0 or count==len(word):
            return True
        else:
            return False
        