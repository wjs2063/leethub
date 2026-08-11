class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        for s in num:
            # 작은놈을 넣어야하니 
            while stack and k and stack[-1] > s:
                stack.pop()
                k -= 1
            stack.append(s)
        
        if k :
            stack = stack[:-k]
        val = "".join(stack).lstrip('0')
        return val if val else "0"
        
        

        


        