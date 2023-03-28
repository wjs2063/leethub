# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        from collections import defaultdict
        seen = defaultdict(int)
        def dfs(root):
            if not root:return
            seen[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        m = max(seen.values())
        for i,v in seen.items():
            if v == m:
                ans.append(i)
        return ans