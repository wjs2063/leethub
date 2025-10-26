# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        candidate = []

        # inorder로 순회후 순서다른 두개  
        # root.val 로 소팅 
        # 1 3 2 4 
        # 1 2 3 4 

        def inorder(root:TreeNode):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        node_list = inorder(root)

        def find_swapped_nodes(node_list):
            n = len(node_list)
            # 2개 다른인덱스 찾기 
            # 1 10  8  5 12 
            # 1 3 2 4 
            x,y = None,None
            for i in range(n - 1):
                if node_list[i + 1] < node_list[i]:
                    y = node_list[i + 1]
                    if x is None:
                        x = node_list[i]
                    else:
                        return x,y
            return x,y
                


        
        x,y = find_swapped_nodes(node_list)
        # always x > y 
        def recover_bst_node(root:TreeNode,cnt):
            nonlocal x,y
            if root:
                if root.val == x or root.val == y :
                    root.val = y if root.val == x else  x 
                    cnt -= 1
                    if cnt == 0 : return 
                recover_bst_node(root.left,cnt)
                recover_bst_node(root.right,cnt)
        recover_bst_node(root,2)



        



        