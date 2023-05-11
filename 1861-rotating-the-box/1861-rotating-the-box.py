class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rotate_box = list(zip(*box))
        # 아래에서 부터 시작 
        n = len(rotate_box)
        m = len(rotate_box[0])
        rotate_box = [list(rt)[::-1] for rt in rotate_box]
        #print(rotate_box)
        for c in range(m):
            for r in range(n - 1,-1,-1):
                # 현재 돌이고 다음칸이 빈공간일떄만 down 가능 
                # 떨어질수있을때까지 떨어져보자
                if rotate_box[r][c] == "#":
                    nr,nc = r + 1,c
                    while 0 <= nr < n:
                        # 돌
                        if rotate_box[nr][nc] in ["#","*"]:
                            nr -= 1
                            break
                        nr += 1
                    if nr >= n :
                        nr -= 1
                    rotate_box[nr][nc] = "#"
                    if (r,c) != (nr,nc):
                        rotate_box[r][c] = "."
                    #print(r,c,rotate_box,nr,nc)
        return rotate_box
                
                
                