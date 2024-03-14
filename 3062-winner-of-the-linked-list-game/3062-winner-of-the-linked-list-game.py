# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd,even = 0,0
        
        while head:
            e,o = head.val,head.next.val 
            if o > e :odd += 1
            if e > o :even += 1
            head = head.next.next
        
        if odd > even :
            return "Odd"
        elif odd == even :
            return "Tie"
        return "Even"