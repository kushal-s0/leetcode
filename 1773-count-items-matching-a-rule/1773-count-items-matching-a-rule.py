class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        if ruleKey=="type":
            a=0
        elif ruleKey=="color":
            a=1
        else:
            a=2
        for i in range(len(items)):
            if items[i][a]==ruleValue:
                count+=1
        return count
        