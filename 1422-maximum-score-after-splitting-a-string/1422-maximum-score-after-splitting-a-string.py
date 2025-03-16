class Solution:
    def maxScore(self, s: str) -> int:
        zero = [0] * (len(s) + 1)
        one = [0] * (len(s) + 1)
        # 0 ~ i 까지의 sum 
        for i,v in enumerate(s):
            zero[i + 1] = zero[i]
            one[i + 1] = one[i]
            if v == "1":
                one[i + 1] += 1
            else:
                zero[i + 1] += 1
        ans = 0 
        print(one,zero)
        # 0 ~ i , i + 1 ~ n
        for idx in range(1,len(s)):
            ans = max(ans,zero[idx] + one[-1] - one[idx])
        return ans 
         
        