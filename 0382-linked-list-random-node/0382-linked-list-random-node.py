# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import random

    def __init__(self, head: Optional[ListNode]):
        self.head=head
        

    def getRandom(self) -> int:
        val=self.head.val
        curr=self.head
        wall=1
        while curr:
            if random.randint(0,wall-1)==0:
                val=curr.val
            curr=curr.next
            wall+=1
        return val

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()