# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        INF = float("-inf")
        lv = [INF]*(10**4 + 1)
        def dfs(root,depth):
            if not root : return
            nonlocal lv
            lv[depth] = max(root.val,lv[depth])
            dfs(root.left,depth + 1)
            dfs(root.right,depth + 1)
        dfs(root,0)
        ans = []
        for i,v in enumerate(lv):
            if v == INF:return ans 
            ans.append(v)
        return ans
        
        