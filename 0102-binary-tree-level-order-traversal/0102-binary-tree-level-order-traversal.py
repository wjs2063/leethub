# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        memo = defaultdict(list)
        def dfs(root,level):
            if not root:return
            dfs(root.left,level + 1)
            memo[level].append(root.val)
            dfs(root.right,level + 1)
        dfs(root,0)
        ans = []
        for key in sorted(memo.keys()):
            ans.append(memo[key])
        return ans
            