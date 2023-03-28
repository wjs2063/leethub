# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        n,m = m,n
        
        arr = [[-1]*m for _ in range(n)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        i = 0
        x,y = 0,0
        def in_range(x,y):
            if 0 <= x < n and 0 <= y < m :return 1
            return 0
        
        while head:
            if not in_range(x,y) or arr[x][y] != -1:
                #backward
                x,y = x - dirs[i][0],y - dirs[i][1]
                #direction change
                i = (i + 1) % 4
                x,y = x + dirs[i][0],y + dirs[i][1]
            arr[x][y] = head.val
            x,y = x + dirs[i][0],y + dirs[i][1]
            head = head.next
        return arr
            
            
            
        