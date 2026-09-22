# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        prev=None
        curr=head
        while curr:
            n=curr.next
            curr.next=prev
            prev=curr
            curr=n
        head=prev

        curr=head
        m=head.val
        while curr and curr.next:
            if curr.next.val<curr.val:
                curr.next=curr.next.next
            else:
                curr=curr.next

        prev=None
        curr=head
        while curr:
            n=curr.next
            curr.next=prev
            prev=curr
            curr=n
        head=prev

        return head

