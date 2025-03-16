# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque 
        level = defaultdict(list)
        ans = []

        def dfs(root:Optional[TreeNode],_level) -> None :
            if root is None:return 
            level[_level].append(root.val)
            dfs(root.left,_level + 1)
            dfs(root.right,_level + 1)
        dfs(root,0)
        for k,v in level.items():
            ans.append(max(v))
        return ans


        