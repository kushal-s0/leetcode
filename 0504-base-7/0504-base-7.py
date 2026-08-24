class Solution:
    def convertToBase7(self, num: int) -> str:
        if num<0:
            num=-num
            st=""
            a=num%7
            st+=str(a)
            r=num//7
            while r!=0:
                a=r%7
                st+=str(a)
                r=r//7
            st+="-"
            return st[::-1]
        else:
            st=""
            a=num%7
            st+=str(a)
            r=num//7
            while r!=0:
                a=r%7
                st+=str(a)
                r=r//7
            return st[::-1]


        