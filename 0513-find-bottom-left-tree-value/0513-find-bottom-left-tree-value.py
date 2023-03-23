# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = []
        q = deque([root])
        while q:
            x = q.popleft()
            ans.append(x.val)
            if x.right:
                q.append(x.right)
            if x.left:
                q.append(x.left)
        return ans[-1]

        