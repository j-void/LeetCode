# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return;
        node = head
        prev = None
        all_nodes = []
        while node:
            all_nodes.append(node)
            node = node.next
        
        for i in range(len(all_nodes)):
            j = i
            while j > 0 and all_nodes[j-1].val > all_nodes[j].val:
                all_nodes[j-1], all_nodes[j] = all_nodes[j], all_nodes[j-1]
                j -= 1

        for i in range(1, len(all_nodes)):
            all_nodes[i-1].next = all_nodes[i]
            all_nodes[i].next = None
        return all_nodes[0]

        
