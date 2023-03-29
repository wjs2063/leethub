class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        multiple_prefix = [0] # multiple_prefix[x] := 0 ~ x 까지의 index * value prefix
        s = 0
        for i,v in enumerate(satisfaction):
            s += (i + 1) * v
            multiple_prefix.append(s)
        # s1,s2,s3,s4,s5
        # 1  2  3  4  5  
        #-9 -8 -1 0 5 
        # 1  2  3 4 5  
        # -9 - 16 -3 25 = 
        #  1 2 3 4 5  0번째는 tot 에 저장 
        #  0 1 2 3 4  1번째는 tot 에서 sum(0 ~ n ) 까지 한번뺴주자
        #  0 0 1 2 3  2번째는 
        #  0 0 0 1 2 
        #  0 0 0 0 1 
        #  0 0 0 0 0 
        s = 0 
        arr = [0]
        ans = 0
        for i,v in enumerate(satisfaction):
            s += v
            arr.append(s)
        for i in range(n + 1):
            ans = max(ans,multiple_prefix[n] - multiple_prefix[i] - i*(arr[n] - arr[i]))
        return ans
        