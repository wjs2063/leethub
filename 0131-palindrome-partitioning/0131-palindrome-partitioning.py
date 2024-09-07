import sys 
#sys.setrecursionlimit(10**7)
class Solution:
    
    def is_palindrome(self,s) -> bool:
        return s == s[::-1]
    
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(s,[],result)
        return result
    
    
    def dfs(self,s,sub_answer,result):
        if len(s) == 0 :
            result.append(sub_answer)
            return 
        
        for idx in range(1,len(s) + 1):
            if self.is_palindrome(s[:idx]):
                self.dfs(s[idx:],sub_answer + [s[:idx]],result)
        
            
        