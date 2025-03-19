# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(list)
        res = []
        def dfs(root:TreeNode):
            if root is None : return 
            nonlocal graph 
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        q = deque([(target.val,0)])
        vis = set()
        vis.add(target.val)
        while q :
            node,dist = q.popleft()
            if dist == k :
                res.append(node)

            for next_node in graph[node]:
                if next_node in vis : continue 
                vis.add(next_node)
                q.append((next_node,dist + 1))
        return res
