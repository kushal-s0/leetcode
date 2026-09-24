# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        s,f=head,head
        m=0
        while f and f.next:
            f=f.next.next
            s=s.next
        curr,prev=s,None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        while prev:
            m=max(m,head.val+prev.val)
            prev=prev.next
            head=head.next
        return m 