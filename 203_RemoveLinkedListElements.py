# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        node = head
        prev = dummy
        while node:
            if node.val == val:
                prev.next = node.next
                node = node.next
            else:
                prev.next = node
                prev = node
                node = node.next
        return dummy.next
        
