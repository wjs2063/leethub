class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        arr = []
        p = [0] * n 
        for i,v in enumerate(corridor):
            if v == "S":
                p[i] = 1
        right = p[:]
        for i in range(n - 2,-1,-1):
            right[i] += right[i + 1]
        
        idx = 0
        cnt = 0
        last = -1
        # 아무것도없거나, 홀수개면 불가능하지 
        if right[0] == 0 or right[0] % 2 == 1:return 0
        while idx < n:
            cnt += p[idx]
            # 만약 처음으로 2개가 되는 순간에 기록
            if cnt == 2 and last == -1:
                last = idx 
            # 2에서 3이되는순간, 그리고 우측에 남은게 2개이상이라면?
            if cnt > 2 and right[idx] >= 2:
                arr.append(idx - last)
                # 초기화 
                last = -1
                cnt = 1
            idx += 1
        ans = 1
        MOD = int(1e9) + 7
        for v in arr:
            ans = (ans * v) % MOD
        return ans
        
            
                
            
            
            
                
            
                
                
        