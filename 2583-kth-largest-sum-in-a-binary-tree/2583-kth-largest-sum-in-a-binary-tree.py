# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        lv = [0]*(10**5 + 1)
        def bfs(root):
            q = deque([(root,1)])
            nonlocal lv
            lv[1] = root.val
            while q:
                x,cnt = q.popleft()
                if x.left:
                    lv[cnt + 1] += x.left.val
                    q.append((x.left,cnt + 1))
                if x.right:
                    lv[cnt + 1] += x.right.val
                    q.append((x.right,cnt + 1))
        bfs(root)
        if lv[k] == 0:return -1
        return sorted([i for i in lv if i != 0],reverse = True)[k - 1]
        
                