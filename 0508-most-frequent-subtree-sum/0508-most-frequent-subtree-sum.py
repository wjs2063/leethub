# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        memo = defaultdict(int)
        
        def dfs(root):
            if not root:return 
            
            cnt = root.val
            if root.left :
                cnt += dfs(root.left)
            if root.right:
                cnt += dfs(root.right)
            memo[cnt] += 1
            return cnt 
        dfs(root)
        ans = []
        m = max(memo.values())
        for key in memo:
            if memo[key] == m:
                ans.append(key)
        return ans
        
        
            