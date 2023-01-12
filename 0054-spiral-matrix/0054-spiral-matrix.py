class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n , m = len(matrix), len(matrix[0])
        cnt = n*m - 1
        visited = [ [ False ]*m for _ in range(n)]
        i,j = 0,0
        answer = [matrix[0][0]]
        visited[0][0] = True
        while cnt > 0 :
            # right
            while j + 1 < m and not visited[i][j + 1]:
                visited[i][j + 1] = True
                answer.append(matrix[i][j + 1])
                j += 1
                cnt -= 1
                
            # down
            while i + 1 < n and not visited[i + 1][j]:
                visited[i + 1][j] = True
                answer.append(matrix[i + 1][j])
                i += 1
                cnt -= 1
                
            # left
            while j - 1 >= 0 and not visited[i][j - 1]:
                visited[i][j - 1] = True
                answer.append(matrix[i][j - 1])
                j -= 1
                cnt -= 1
                
            # up
            while i - 1 >= 0 and not visited[i - 1][j]:
                visited[i - 1][j] = True
                answer.append(matrix[i - 1][j])
                i -= 1
                cnt -= 1
                
        return answer
            