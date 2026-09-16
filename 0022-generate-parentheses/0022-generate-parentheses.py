class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        brackets=[""]*(n*2)
        result = []
        def solve(idx,total,brackets,result):
            if idx>=len(brackets):
                if total==0:
                    result.append("".join(brackets))
                return 
            if total>len(brackets)//2:
                return
            elif total<0:
                return
            brackets[idx]="("
            summ=total+1
            solve(idx+1,summ,brackets, result)
            brackets[idx]=")"
            summ=total-1
            solve(idx+1,summ,brackets, result)
        solve(0, 0, brackets, result)
        return result