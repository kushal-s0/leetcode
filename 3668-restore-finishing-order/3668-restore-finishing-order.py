class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        i=0
        result=[]
        while len(result)!=len(friends):
            if order[i] in friends:
                result.append(order[i])
            i+=1
        return result