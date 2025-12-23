class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """
        시작, 끝, 점수
        선택은 최대 2번만 가능, 점수를 최대로 하고싶어
        총 개수는 어차피 10^5 
        정렬 : 

        1개가 압도적으로 높은경우도있고 

        2개를 잘 선택하면 그게 최대점수일수도있고 

        근데 개수가 10^5 이니 nlogn 안에 풀어야함

        시작기준으로 제일 빠르게 시작하는 애들먼저 넣고 

        힙에는 종료시점과, 점수만 넣어 (후보군)

        매 이벤트마다 후보군을 꺼내서 계속 확인함 -> 
        """
        import heapq 

        h = []
        events.sort(key=lambda x:x[0])
        max_score = 0 
        ans = 0
        for event in events:

            # 현재 이벤트 기준으로 겹치지않는 이벤트중 가장 큰 점수갱신 
            while h and h[0][0] < event[0]:
                max_score = max(max_score,h[0][1])
                heapq.heappop(h)
            
            ans = max(ans,max_score + event[2])

            heapq.heappush(h,(event[1],event[2]))
        return ans

        






        

        

        