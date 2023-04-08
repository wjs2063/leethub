class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def solve(strs):
            stack = []
            
            for i,v in enumerate(strs):
                if v == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(v)
            return stack 
        
        return solve(s) == solve(t)