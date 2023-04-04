class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        seen = set()
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        x,y = 0,0
        d = 0
        for ins in instructions*5:
            if ins == "L":
                d = (d - 1)  % 4
            elif ins == "R":
                d = (d + 1) % 4
            else:
                x,y = x + dirs[d][0],y + dirs[d][1]
        return (x,y) == (0,0) or d != 0
        
            
        