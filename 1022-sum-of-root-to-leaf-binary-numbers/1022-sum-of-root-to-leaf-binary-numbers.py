# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        s = 0
        #vlr
        answer = ""
        def dfs(root,answer):
            nonlocal s
            answer += str(root.val)
            if root.left == None and root.right == None:
                for i in range(len(answer)):
                    s += int(answer[len(answer) - 1 - i]) * 2 ** i 
            if root.left :
                dfs(root.left,answer)
            if root.right:
                dfs(root.right,answer)
        dfs(root,answer)
        return s 

        