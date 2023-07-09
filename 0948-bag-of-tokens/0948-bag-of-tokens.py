class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = 0
        ticket = 0
        l,r = 0,len(tokens) - 1
        tokens.sort()
        while l <= r :
            token = tokens[l]
            if token <= power:
                
                ticket += 1
                power -= token
                l += 1
            elif ticket :
                ticket -= 1
                power += tokens[r]
                r -= 1
            else:
                break 
            ans = max(ans,ticket)
        return ans