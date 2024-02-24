from collections import defaultdict,deque
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        network = defaultdict(list)
        
        for x,y,atTime in meetings:
            network[x].append([y,atTime])
            network[y].append([x,atTime])
        
        INF = int(1e10)
        # shared_time[x] := x 라는 사람이 비밀을 알게되는 순간
        shared_time = [INF] * (n)
        # 0,firstPerson 은 시각 0에서 공유
        shared_time[0] = 0
        shared_time[firstPerson] = 0 

        q = deque([(0,0),(0,firstPerson)])
        
        
        while q :
            time,p = q.popleft()
            
            for np,nt in network[p]:
                if nt >= time and shared_time[np] > nt :
                    shared_time[np] = nt 
                    q.append([nt,np])
        ans = [person for person,v in enumerate(shared_time) if v != INF]
        return ans