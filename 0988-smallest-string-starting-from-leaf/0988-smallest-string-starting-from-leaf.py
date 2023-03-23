# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []
        
        def dfs(root,s):
            if root.left == None and root.right == None :
                ans.append(chr(root.val + ord('a')) + s)
                return 
            if root.left:
                dfs(root.left,chr(root.val + ord('a')) + s )
            if root.right:
                dfs(root.right,chr(root.val + ord('a')) + s )
        dfs(root,"")
        ans.sort(key = lambda x:x)
        return ans[0]
            
            