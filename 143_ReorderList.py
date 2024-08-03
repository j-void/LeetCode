# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        list_nodes = []
        node = head
        while node:
            list_nodes.append(node)
            node = node.next
        
        prev = None
        i,j = 0,len(list_nodes)-1
        if i == j:
            return head
            
        while i<=j:
            if i == j:
                prev.next = list_nodes[i]
                list_nodes[i].next = None
                break
            print(list_nodes[i].val, list_nodes[j].val, prev)
            list_nodes[i].next = list_nodes[j]
            if prev:
                prev.next = list_nodes[i]
            prev = list_nodes[j]
            i += 1
            j -= 1
        
        list_nodes[i].next = None
        # print(list_nodes[i].val)
