class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0 
        
        n,m = len(mat),len(mat[0])
        #print(list(zip(*mat)))
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if (sum(mat[i]) - 1 == 0) and (sum(list(zip(*mat))[j]) - 1 == 0):
                        res += 1
        return res