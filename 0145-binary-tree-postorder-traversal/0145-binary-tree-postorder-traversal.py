# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def dfs(root):
            nonlocal answer
            if root == None:
                return
            dfs(root.left)
            dfs(root.right)
            answer.append(root.val)
        dfs(root)
        return answer
        