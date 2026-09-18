class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        numbers={
            "1": [],                "2": ['a', 'b','c'],    "3": ['d','e','f'],
            "4": ['g','h','i'],     "5": ['j','k','l'],     "6": ['m','n','o'],
            "7": ['p','q','r','s'], "8": ['t','u','v'],     "9": ['w','x','y','z']
        }
        result=[]
        self.bt(0,[],numbers,digits,result)
        return result
    def bt(self,idx,subset,numbers,d,result):
        if idx>=len(d):
            result.append("".join(subset))
            return
        for char in numbers[d[idx]]:
            subset.append(char)
            self.bt(idx+1,subset,numbers,d,result)
            subset.pop()