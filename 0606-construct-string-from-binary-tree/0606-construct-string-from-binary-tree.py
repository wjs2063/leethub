# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root):
            if not root :return ""
            temp = str(root.val)
            
            if root.left :
                temp += "(" + dfs(root.left) + ")"
            if root.left == None and root.right :
                temp += "()" + "(" + dfs(root.right) + ")"
            elif root.left and root.right:
                temp += "(" + dfs(root.right) + ")"
            return temp
        return dfs(root)
            
            
                