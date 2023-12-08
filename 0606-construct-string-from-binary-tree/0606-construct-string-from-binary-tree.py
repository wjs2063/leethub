# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if root is None:return ""

            
            
            temp = str(root.val)
            
            # 둘다 없으면 그대로 return 
            if root.left is None and root.right is None :
                return temp
            temp += '(' + preorder(root.left) + ')'
            if root.right :
                temp += '(' + preorder(root.right) + ')'
            return temp
        return preorder(root)