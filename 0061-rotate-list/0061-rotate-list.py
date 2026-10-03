# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k==0:
            return head
        temp=head
        count=0
        while temp:
            temp=temp.next
            count+=1
        k = k % count
        if k == 0:
            return head
        n=count-k-1
        s=head
        while n>0:
            s=s.next
            n-=1
        temp=s
        while temp.next:
            temp=temp.next
        temp.next=head
        head=s.next
        s.next=None
        return head
