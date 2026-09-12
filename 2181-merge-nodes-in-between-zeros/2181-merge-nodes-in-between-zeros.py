# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=head
        r=head.next
        count=0
        while r is not None:
            if r.val==0:
                l.val=count
                if r.next!=None:
                    l=l.next
                else:
                    l.next=None
                count=0
                r=r.next
            else:
                count+=r.val
                r=r.next
        return head
        
            
