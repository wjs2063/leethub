# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        while head:
            arr.append(head.val)
            head=head.next
        
        c = Counter(arr)
        for k in c :
            if c[k] > 1 :
                for _ in range(c[k]):
                    arr.remove(k)
        if len(arr) <= 0 :
            return None
        start = head = ListNode()
        for i,v in enumerate(arr):
            head.val = v 
            
            if i == len(arr) - 1:
                break 
            head.next = ListNode()
            head = head.next 
        return start
            
        