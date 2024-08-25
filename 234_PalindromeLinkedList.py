# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return True
        slow, fast = head, head.next
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        

        if not fast:
            half = slow.next
            slow = prev
        else:
            half = slow.next
        
        slow.next = None
        half = self.reverse(half)

        while head and half:
            if head.val != half.val:
                return False
            head = head.next
            half = half.next
        
        return True
        

    def reverse(self, head):
        prev = None
        node = head
        while node:
            currNext = node.next
            node.next = prev
            prev = node
            node = currNext
        return prev
