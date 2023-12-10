class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for transpose in zip(*matrix):
            ans.append(list(transpose))
        return ans
        