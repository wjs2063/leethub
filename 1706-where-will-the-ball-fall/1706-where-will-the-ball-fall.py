class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        answer = []
        # 1 is right , -1 is left
        for col in range(m):
            row = 0
            flag = True
            for _ in range(n):
                #next direcition
                next_col = col + grid[row][col]
                # 다음방향이 벗어는경우라면
                if next_col < 0 or next_col >= m :
                    answer.append(-1)
                    flag = False
                    break
                # 현재방향과 다음방향이 충돌하는경우
                if grid[row][next_col] * grid[row][col] < 0:
                    answer.append(-1)
                    flag = False
                    break
                col = next_col
                row += 1
            if flag :
                answer.append(col)
        return answer
                
            