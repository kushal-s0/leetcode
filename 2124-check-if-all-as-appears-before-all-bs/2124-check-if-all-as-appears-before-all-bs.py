class Solution:
    def checkString(self, s: str) -> bool:
        b=False
        for char in s:
            if b and char=="a":
                return False
            elif char=="b":
                b=True
        return True