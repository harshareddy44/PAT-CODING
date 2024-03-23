# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        currMax = -99999
        while head:
            # print(arr)
            if len(arr) == 0:
                currMax = head.val
                arr.append(head.val)
            else:
                if head.val > currMax:
                    currMax = head.val
                    arr = [head.val]
                
                else:
                    if head.val > arr[-1]:
                        for i in range(len(arr)-1, -1, -1):
                            if head.val > arr[i]:
                                arr.pop()
                            else:
                                break
                    arr.append(head.val)
            head = head.next
        # print(arr)
        d = n = ListNode()
        for i in arr:
            n.next = ListNode(i)
            n = n.next
        return d.next
