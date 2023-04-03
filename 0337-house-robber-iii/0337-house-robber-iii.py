# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        
        def dfs(root):
            if not root:return 0,0
            #자식을 훔치치않은경우,자식을 훔친경우 두가지 버젼 
            left_0,left_1 = dfs(root.left)
            right_0,right_1 = dfs(root.right)
            # 선택지, 현재 root 를 훔치는경우,훔치지않는경우,
            #자식을 훔치지않은 경우는 현재를 훔쳐볼수있다.
            # 자식을 훔쳤으면 현재는 훔칠수없다
            return max(left_0,left_1) + max(right_0,right_1),root.val + left_0 + right_0
        return max(dfs(root))