# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        ans = 0
        def dfs(root) -> Tuple:
            # sum, cnt 
            if root is None :  return [0,0]
            nonlocal ans 
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            ans = max(ans,(root.val + l[0] + r[0]) / (1 + l[1] + r[1]))
            return [root.val + l[0] + r[0],1 + l[1] + r[1]]
        dfs(root)
        return ans
            