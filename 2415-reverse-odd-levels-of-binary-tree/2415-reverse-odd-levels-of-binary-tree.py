# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        graph = defaultdict(deque)
        def level_wise(root,graph,level):
            if root == None:
                return
            graph[level].append(root.val)
            level_wise(root.left,graph,level + 1)
            level_wise(root.right,graph,level + 1)
        level_wise(root,graph,0)
        for i in graph:
            if i % 2 == 1:
                graph[i].reverse()
        ## ??
        def dfs(graph,level):
            if len(graph[level]) == 0:
                return
            root = TreeNode(graph[level].popleft())
            root.left = dfs(graph,level + 1)
            root.right = dfs(graph,level + 1)
            return root
               
        return dfs(graph,0)
