"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import defaultdict
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        cc = defaultdict(list)
        def dfs(root,level):
            
            nonlocal cc
            if root == None:
                return 
            cc[level].append(root.val)
            for child in root.children:
                dfs(child,level + 1)
        dfs(root,0)
        answer = []
        for i in cc:
            answer.append(cc[i])
        return answer
            
            