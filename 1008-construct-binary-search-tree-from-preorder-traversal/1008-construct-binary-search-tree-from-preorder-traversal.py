# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        #partition ->  smaller and  greater
        if preorder[0] < preorder[1]:
            root.right = self.bstFromPreorder(preorder[1:])
        else :
            gr = 0
            for i in range(1,len(preorder)):
                if preorder[0] < preorder[i]:
                    gr = i
                    break
            if gr >= 1:
                root.left = self.bstFromPreorder(preorder[1:gr])
                root.right = self.bstFromPreorder(preorder[gr:])
            else:
                root.left = self.bstFromPreorder(preorder[1:])


        return root
