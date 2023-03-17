class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        """
        풀이전략 : 
        1.모든땅을 그룹화시킨다 -> grid 에 땅의 인덱스를 저장
        2. dictionary 구조에 그룹화한 땅의 넓이를 저장한다.
        3. 그다음 2중포문을 돌면서 0인 부분에 대해서 1로바꿨을때 각 인접지역에서 올수있는 땅들을 계산한다.
        """
        def in_range(i,j):
            if 0 <= i < n and 0 <= j < n:
                return True
            return False
        # 땅넓이 계산
        def dfs(i,j,idx):
            cnt = 1
            grid[i][j] = idx
            for ni,nj in [(i + 1,j),(i - 1,j),(i,j + 1),(i,j - 1)]:
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                    cnt += dfs(ni,nj,idx)
            return cnt 
        memo = dict()
        # 땅이 0 과 1이므로 2부터시작
        idx = 2
        for i in range(n):
            for j in range(n):
                # 현재 지점이 땅이라면 dfs 수행
                if grid[i][j] == 1:
                    memo[idx] = dfs(i,j,idx)
                    idx += 1
        # if empty 
        memo[-1] = 0
        ans = max(memo.values())
        
        for i in range(n):
            for j in range(n):
                # i,j 가 0이라면 이제 1걔씩 바꾼경우를 생각해본다
                if grid[i][j] == 0:
                    vis = {grid[ni][nj] for ni,nj in [(i + 1,j),(i - 1,j),(i,j + 1),(i,j - 1)] if in_range(ni,nj) and grid[ni][nj] > 1}
                    ans = max(ans,1 + sum(memo[i] for i in vis))
        return ans
        
        
        
        