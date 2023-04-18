# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        def dfs(root,mini,maxi):
            if root:
                nonlocal ans
                mini,maxi = min(mini,root.val),max(maxi,root.val)
                ans = max(ans,maxi - mini)
                dfs(root.left,mini,maxi)
                dfs(root.right,mini,maxi)
        dfs(root,int(1e10),0)
        return ans
                
        
        
            
            
            