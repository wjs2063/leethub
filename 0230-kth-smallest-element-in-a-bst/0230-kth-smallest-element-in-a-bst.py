# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = []

        def dfs(root):
            nonlocal answer
            if root is None :return 
            dfs(root.left)
            dfs(root.right)
            answer.append(root.val)
        dfs(root)
        answer.sort()
        return answer[k - 1]
             


        