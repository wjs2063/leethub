class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a,b = nums[0],nums[nums[0]]
        """
        핵심 포인트 Floyds' cycle detection 
        slow pointer 
        fast pointer 
        하나는 1개씩 전진
        다른하나는 2개씩전진
        """
        # 일단은 싸이클이 무조건 있다는 전제하에 진행
        while a != b:
            a,b = nums[a],nums[nums[b]]
        a = 0
        while a != b:
            a = nums[a]
            b = nums[b]
        return a