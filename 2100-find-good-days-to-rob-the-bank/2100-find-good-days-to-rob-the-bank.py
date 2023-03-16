class Solution:
    def goodDaysToRobBank(self, a: List[int], time: int) -> List[int]:
        # non-increase
        left = [0]
        # non -decrease
        right = [0]
        cnt = 0
        n = len(a)
        for i in range(1,n):
            if a[i - 1] >= a[i]:
                cnt += 1
            else:
                cnt = 0
            left.append(cnt)
        cnt = 0
        for i in range(n - 1,0,-1):
            if a[i - 1] <= a[i] :
                cnt += 1
            else:
                cnt = 0
            right.append(cnt)
        # 인덱스 역전
        right = right[::-1]
        return [i for i in range(n) if left[i] >= time and right[i] >= time]
            
                    
        