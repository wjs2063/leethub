# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.val = 0
    
    def sum_of_tree(self,root:Optional[TreeNode]) -> int:
        if root is None :return 0
        sum_of_left_tree = self.sum_of_tree(root.left)
        sum_of_right_tree = self.sum_of_tree(root.right)
        self.val += abs(sum_of_left_tree - sum_of_right_tree)
        return sum_of_left_tree + sum_of_right_tree + root.val
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.sum_of_tree(root)
        
        
        return self.val 
    