class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = Counter(tasks)
        answer = 0
        for t in tasks:
            cnt = tasks[t]
            # x 의 범위는 0 <= x <= n // 2
            flag = True
            for x in range(cnt // 2 + 1):
                if (cnt + x ) % 3 == 0:
                    flag = False
                    answer += (cnt + x) // 3
                    break
            if flag:
                return -1
        return answer
            
        
            