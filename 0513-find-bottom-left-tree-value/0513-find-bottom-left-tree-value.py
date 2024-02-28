# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import defaultdict
        max_level = 0 
        left_order_dict = defaultdict(list)
        
        def dfs(root,left_order_dict,lv):
            if root is None : return
            nonlocal max_level
            #LVR 
            dfs(root.left,left_order_dict,lv + 1)
            # ROOT
            if lv > max_level:
                max_level = lv
            left_order_dict[lv].append(root.val)
            dfs(root.right,left_order_dict,lv + 1)
        dfs(root,left_order_dict,0)
        return left_order_dict[max_level][0]