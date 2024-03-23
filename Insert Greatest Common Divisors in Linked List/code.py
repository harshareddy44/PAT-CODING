# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr1 = head
        itr2 = head
        while itr1.next:
            p = itr1.val
            q = itr1.next.val
            node = ListNode(gcd(p, q), itr1.next)
            itr1.next = node
            itr1 = itr1.next.next
        
        return head
