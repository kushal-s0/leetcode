class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=1
        for i in range(len(sentences)):
            temp=1
            for j in range(len(sentences[i])):
                if sentences[i][j]==" ":
                    temp+=1
            if count<temp:
                count=temp
        return count
