class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        n = len(tickets)
        while tickets[k] :
            s = 0
            for i in range(n):
                if tickets[i] :
                    tickets[i] -= 1
                    s += 1
                if tickets[k] == 0 :
                    ans += s 
                    return ans
            ans += s
        return ans
                