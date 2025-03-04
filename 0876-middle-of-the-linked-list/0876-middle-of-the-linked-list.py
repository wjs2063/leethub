# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_node : list[ListNode] = list()
        
        while head:
            list_node.append(head)
            head = head.next
        n = len(list_node)
        if n == 0 :
            return 
        return list_node[n // 2]
        