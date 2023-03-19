# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # dfs(root) := if we have x coins on root -> then we have to move x - 1
        # we don't need to know where to go because whatever answer is exist
        ans = 0
        # borrow -> negative
        def dfs(root):
            if root == None:
                return 0
            nonlocal ans
            l = dfs(root.left)
            r = dfs(root.right)
            tot = root.val + l + r
            # 움직여야 하는 횟수 
            ans += abs(l) + abs(r)
            return tot - 1
        dfs(root)
        return ans
        