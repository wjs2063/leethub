# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        from collections import defaultdict
        def find(a):
            if a not in parent:
                parent[a] = a
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        def union(a,b):
            x,y = find(a),find(b)
            parent[x] = y 
        
        parent = defaultdict(int)
        tree = defaultdict(list)
        for p,c,is_left in descriptions:
            tree[p].append([c,is_left])
            parent[c] = p
        
        root = find(descriptions[0][0])
        
        def dfs(r):
            root = TreeNode(r)
            for c,is_left in tree[r]:
                if is_left == 1:
                    root.left = dfs(c)
                else:
                    root.right = dfs(c)
            return root
        return dfs(root)
        
        
        