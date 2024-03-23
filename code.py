# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        main = head
        itr1 = head
        summ = 0
        while itr1.next:
            if itr1.val == 0 and itr1 != head:
                summ += itr1.val
                main.val = summ
                main = main.next
                summ = 0
            summ += itr1.val
            itr1 = itr1.next
        
        main.val = summ
        main.next = None
        return head
