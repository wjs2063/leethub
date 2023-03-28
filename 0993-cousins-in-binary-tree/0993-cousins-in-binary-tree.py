# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import defaultdict
        table = defaultdict(set)
        # same depth and different parent 
        parent = [0]*(101)
        c = [0]*(101)
        def dfs(root,p,depth):
            if not root:return
            parent[root.val] = p
            c[root.val] = depth
            dfs(root.left,root.val,depth + 1)
            dfs(root.right,root.val,depth + 1)
        dfs(root,-1,0)
        
        return c[x] == c[y] and parent[x] != parent[y]
        