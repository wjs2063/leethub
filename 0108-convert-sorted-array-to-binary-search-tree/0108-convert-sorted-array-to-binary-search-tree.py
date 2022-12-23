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
        def reconfig(nums):
            if len(nums) == 0:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = reconfig(nums[:mid])
            root.right = reconfig(nums[mid + 1:])
            return root
        root = reconfig(nums)
        return root
        
            
            