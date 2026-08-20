class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            stack.append(num)

            while len(stack) > 1 and stack[-2] == stack[-1]:
                _val = stack.pop()
                stack[-1] += _val
        return stack 