# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
    #     odd = []
    #     even = []
    #     node = head
    #     i = 0
    #     while node:
    #         if i%2 == 0:
    #             even.append(node.val)
    #         else:
    #             odd.append(node.val)
    #         node = node.next
    #         i += 1
    #     node = head
    #     oddEven = even + odd
    #     for i in range(len(oddEven)):
    #         node.val = oddEven[i]
    #         node = node.next
    #     return head
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        even_head = head
        odd_head = head.next
        odd_head_new = odd_head
        node = head.next.next
        i = 2
        while node:
            if i % 2 == 0:
                even_head.next = node
                even_head = node
            else:
                odd_head.next = node
                odd_head = node
            node = node.next
            i += 1
        even_head.next = odd_head_new
        odd_head.next = None
        return head
        
