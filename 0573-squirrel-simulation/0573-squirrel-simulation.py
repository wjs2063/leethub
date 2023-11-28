class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        r = height
        c = width
        tx,ty = tree
        sx,sy = squirrel
        n = len(nuts)
        case = []
        for i,(nx,ny) in enumerate(nuts):
            # 나무와 도토리(i번쨰) 사이거리
            dist = abs(nx - tx) + abs(ny - ty)
            case.append([dist,i])
        res = 0
        for i,v in enumerate(case):
            res += 2 * v[0]
        ans = int(1e10)
        for i,(nx,ny) in enumerate(nuts):
            # 편도 거리 
            d = abs(nx - tx) + abs(ny -ty)
            ans = min(ans,res - d + abs(nx - sx) + abs(ny - sy))
        return ans
        
    