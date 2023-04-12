class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        ans = []
        d = 0 
        dx,dy = 1,-1
        
        while d < n + m - 1 :
            r,c = 0 if d < m else d - m + 1, d if d < m else m - 1
            sub = []
            rr,cc = r,c
            while 0 <= rr < n and 0 <= cc < m :
                sub.append(mat[rr][cc])
        
                rr += dx
                cc += dy 
            if d % 2 == 0 :
                ans.extend(sub[::-1])
            else:
                ans.extend(sub)
            d += 1
        return ans
            
            
        
        
        
        
        
        