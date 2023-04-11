class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i,v in enumerate(s):
            stack.append(v)
            if len(stack) > 1 and stack[-1] == "*":
                del stack[-2:]
        return "".join(stack)