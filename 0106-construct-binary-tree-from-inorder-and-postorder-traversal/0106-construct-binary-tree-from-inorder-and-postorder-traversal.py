# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # postorder 특징 : 항상 LRV 형태이므로 마지막원소가 root 이다
        # 여기서 LR 을 구분해야하는데 이것을 inorder 배열로 힌트를 얻는다
        # inorder : LVR 이므로 V 기준으로 나뉜다.
        # V 인덱스 기준으로 분리한다.
        n = len(inorder)
        memo = dict()
        for i,v in enumerate(inorder):
            memo[v] = i
        
        def make_tree(l,r):
            if l > r  :return
            v = postorder.pop()
            idx = memo[v]
            root = TreeNode(v)
            root.right = make_tree(idx + 1,r)
            root.left = make_tree(l,idx - 1)
            """
            root.left = make_tree(l,idx - 1)
            root.right = make_tree(idx + 1,r)
            """
            
            return root
        return make_tree(0,n - 1)
            
            
            
                
            
            