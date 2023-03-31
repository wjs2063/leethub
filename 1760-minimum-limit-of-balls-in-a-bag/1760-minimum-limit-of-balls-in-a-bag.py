class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        sn,en = 1,max(nums)
        """
        패널티가 mid 일떄 
        원소를 
        mid , A - mid 로 나누고 
        A - mid 를 또 mid , A - 2*mid 로 나누고 하다보면 결국 mid 로 나눈 몫이된다
        예를들어면 9 일때 
        3,6 -> 3 ,3 일때 답은 2개다 
        """
        ans = 0
        while sn <= en:
            mid = (sn + en) // 2
            #패널티가 mid 라고 가정하자
            if sum((v - 1) // mid for v in nums) <= maxOperations:
                ans = mid
                en = mid - 1
            else:
                sn = mid + 1
        return ans
                    
            