# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #slicing vs index solution
        #reconfig func -> input : arr
        def reconfig(nums,l,r):
            if l > r :return
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = reconfig(nums,l,mid - 1)
            root.right = reconfig(nums,mid + 1,r)
            return root
        root = reconfig(nums,0,len(nums) - 1)
        return root
        
            
            