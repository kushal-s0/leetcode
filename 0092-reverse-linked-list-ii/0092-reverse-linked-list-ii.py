# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left==right:
            return head
        c=head
        prev=None
        i=1
        while i<left:
            prev=c
            c=c.next
            i+=1
        l=prev
        r=c
        while i<=right:
            temp=c.next
            c.next=prev
            prev=c
            c=temp
            i+=1
        if l:
            l.next=prev
        else:
            head=prev
        r.next=c   
        return head


            
                