class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        # 현재방향
        obs = set()
        for i,v in enumerate(obstacles):
            obstacles[i] = tuple(v)
            obs.add(obstacles[i])
        x,y = 0,0
        ans = 0
        i = 0
        for command in commands:
            if command == -2:
                i = (i - 1) % 4
            elif command == -1:
                i = (i + 1) % 4
            else:
                while command:
                    x,y = x + dirs[i][0],y + dirs[i][1]
                    command -= 1
                    if (x,y) in obs:
                        x,y = x - dirs[i][0],y - dirs[i][1]
                        break
            print(x,y,i)
            ans = max(ans,abs(x)**2 + abs(y)**2)
        return ans
                
                
                
        