# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        
        def dfs(root) -> set:
            nonlocal ans 
            if root is None : return set()
            
            left_set = dfs(root.left)
            right_set = dfs(root.right)
            
            union_set = left_set | right_set | {root.val}
            if len(union_set) == 1 :
                ans += 1
                return union_set
            return union_set
        dfs(root)
        return ans
                
            
            