class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import defaultdict,deque
        return self.breadSearch(deadends=deadends,target=target)

    def breadSearch(self,deadends : List[str],target:str) -> int :
        start = "0000"
        answer = -1
        if start in deadends:return answer
        q = deque([(start,0)])
        visit, deadends_set = set(['0000']), set(deadends)
        MOD = 10
        while q :
            dial,step = q.popleft()
            if dial == target:return step
            # 매 순간마다 1,2,3,4 중 어떤것을 갈지 선택을 해야함

            for i in range(4):
                for d in [-1,1]:
                    implemented_digit =  (int(dial[i]) + d ) % MOD
                    new_digit = (dial[:i] + str(implemented_digit) + dial[i + 1:])
                    if new_digit in visit or new_digit in deadends_set:continue
                    q.append((new_digit,step + 1))
                    visit.add(new_digit)
                    if new_digit == target:
                        return step + 1
        return answer



        