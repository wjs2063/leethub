# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head.next
        ans = root = ListNode()
        prev = 0
        while start:
            if prev == 0 :
                root.next = ListNode()
                root = root.next
            root.val += start.val
            prev = start.val
            start = start.next
        return ans.next
                
        