# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        level = [0]*(1 << 7)
        cnt = 0
        def dfs(root,lv):
            nonlocal level,cnt
            level[lv] += 1
            cnt += 1
            if root.left:
                dfs(root.left,lv + 1)
            if root.right:
                dfs(root.right,lv + 1)
        dfs(root,0)
        k = 0
        while 2**(k + 1) - 1 <= cnt:
            k += 1
        # 이제 k - 1 번째 레벨까지 다 차있는지 확인하고 
        # left 가없으면 right 은 진행하지 않는 방식으로 간다.
        for i in range(k):
            if level[i] != 2**i:
                return False
        ans = 0
        def bfs(root):
            nonlocal ans
            q = deque([root])
            while q :
                x = q.popleft()
                if x == None:
                    return
                ans += 1
                q.append(x.left)
                q.append(x.right)
        bfs(root)
        #print(ans,cnt)
        return ans == cnt
            
            
        
        
        
        