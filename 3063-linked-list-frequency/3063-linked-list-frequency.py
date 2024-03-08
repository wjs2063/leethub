# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        v = []
        while head:
            v.append(head.val)
            head = head.next 
        c = Counter(v)
        head = ListNode()
        start = head
        for k in c:
            node = ListNode(c[k])
            start.next = node 
            start = node 
        return head.next
            