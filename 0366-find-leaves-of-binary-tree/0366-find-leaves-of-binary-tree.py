# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        
        def dfs(parent,root):
            if root is None :return
            
                        # if root is leafnode then Cut 
            if root.left is None and root.right is None:
                ans[-1].append(root.val)
                if parent.left is root:
                    parent.left = None 
                elif parent.right is root:
                    parent.right = None 
                return 
            
            dfs(root,root.left)
            dfs(root,root.right)
            
        
        while root:
            ans.append([])
            if root.left is None and root.right is None :
                ans[-1].append(root.val)
                break
            dfs(root,root)
        return ans
            
                
        