"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # L V R 
        from collections import deque 

        if not root:return root
        q = deque([root]) # (level,root)
        
        while q :
            size = len(q)
            # 현재 레벨의 노드 개수만큼만 돌아감 

            for idx in range(size):
                node = q.popleft()

                # 끝점 제외 
                if idx < size - 1:
                    node.next = q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

        