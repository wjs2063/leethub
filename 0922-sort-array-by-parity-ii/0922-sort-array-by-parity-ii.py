class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        
        for i,v in enumerate(nums):
            if v % 2 :
                odd.append(v)
            else:
                even.append(v)
        ans = []
        for i,v in enumerate(even):
            ans.append(v)
            ans.append(odd[i])
        return ans