# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head.next
        prev=head
        while curr:
            g=gcd(curr.val,prev.val)
            newnode=ListNode(g)
            prev.next=newnode
            newnode.next=curr
            prev=curr
            curr=curr.next
        return head

    def gcd(a,b):
        while b!=0:
            a, b = b, a % b
        return a