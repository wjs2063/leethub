class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for i,v in enumerate(s):
            stack.append(v)
            
            while len(stack) > 1 and "".join(stack[-2:]) in ["()","{}","[]"]:
                del stack[-2:]
        return len(stack) == 0
        