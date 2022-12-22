"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        answer = 0
        def dfs(root,cnt):
            if root == None :
                return 
            nonlocal answer 
            answer = max(answer,cnt)
            for child in root.children:
                dfs(child,cnt + 1)
            return 
        dfs(root,1)
        return answer