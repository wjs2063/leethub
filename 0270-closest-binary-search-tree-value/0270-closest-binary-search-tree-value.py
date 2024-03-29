# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = int(1e10)
        ans = int(1e10)
        def dfs(root):
            if root is None :return 
            nonlocal ans
            nonlocal diff
            if abs(target - root.val) <= diff:
                if abs(target - root.val) == diff:
                    ans = min(ans,root.val)
                else:
                    ans = root.val
                diff = abs(target - root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ans