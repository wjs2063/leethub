# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if root is None :return
            if root.left and root.right:
                dfs(root.left)
                dfs(root.right)
            elif root.left is None and root.right is None :
                return 
            else:
                nonlocal ans
                if root.left:
                    ans.append(root.left.val)
                    dfs(root.left)
                else:
                    ans.append(root.right.val)
                    dfs(root.right)
        dfs(root)
        return ans