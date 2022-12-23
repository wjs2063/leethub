# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left,right = [], []
        def dfs(root,temp):
            if root == None :
                return 
            if root.left == None and root.right == None :
                temp.append(root.val)
            dfs(root.left,temp)
            dfs(root.right,temp)
        dfs(root1,left)
        dfs(root2,right)
        return left == right
                