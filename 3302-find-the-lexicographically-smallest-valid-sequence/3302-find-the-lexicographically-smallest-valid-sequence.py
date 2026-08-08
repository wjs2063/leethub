class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        """
        word1 : x1x2...xn
        word2 : y1y2...ym 
        
        m < n 

        # word2문자열인덱스중 X문자열과 일치하는 인덱스배열 
        w2[x] = 

        word 1 의 문자열중 최대1개를 바꿔서 word2와 동일한게 가능한지
        가능하다면 index를 리스트에 담아서 반환 
        """
        n,m = len(word1),len(word2)
        idx = m - 1
        # w2_idx 에는 word2의 인덱스문자열과 매칭되는 word1의 인덱스가 들어감 
        # w2_idx[k] := word2[k] == word1[j] 인 가장 큰j가 들어가있음 
        w2_idx = [-2] * (m)


        for k in range(n - 1, -1, -1):
            if idx >= 0 and word1[k] == word2[idx]:
                w2_idx[idx] = k
                idx -= 1
                 

        # 단 반드시i < j 에 대해서 ws_idx[i] <= ws_idx < j 를 만족해야함        
        # w1문자열을 오른쪽에서부터 순회하면서 최초로 같아지는 word2의 인덱스를 찾아서 w2_idx 배열에 w1의 인덱스를 기록

        ans = []
        jump = 0 # at most 1 
        t = 0
        for i,v in enumerate(word1):
            # t 는 word2길이넘어가면 안되니 방어 
            if t >= m :
                break 
            
            # word2 와 같으면 해당 인덱스 추가 
            if v == word2[t] :
                ans.append(i)
                t += 1
            
            #문자열이 다르다면 점프가능한상태이거나 
            elif jump == 0 and (t == m - 1 or i < w2_idx[t + 1]):
                jump = 1
                ans.append(i)
                t += 1
        if t == m:
            return ans
        return []



        
        


        
        