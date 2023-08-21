# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        # dfs() -> 현재 root 기준,좌 우 자식노드의 최대길이 
        def dfs(root : TreeNode) -> int :
            if not root :return 0
            nonlocal ans 
            
            l,r = 0,0
            
            if root.left : 
                l = dfs(root.left) + 1
            if root.right:
                r = dfs(root.right) + 1
            ans = max(ans,l + r)
            return max(l,r)
        dfs(root)
        return ans
            
            