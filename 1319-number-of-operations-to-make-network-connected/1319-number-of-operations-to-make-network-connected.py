class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        size = [1] * n

        if len(connections) < n - 1:
            return -1

        def find(parents,x):
            if parents[x] != x :
                parents[x] = find(parents,parents[x])
                return parents[x]
            return parents[x]
        def union(parents,a,b):
            pa = find(parents,a)
            pb = find(parents,b)
            
            if pa == pb : return False 

            if size[pa] < size[pb]:
                pa,pb = pb,pa 

            # pb 의 부모는 pa로 
            parents[pb] = pa
            size[pa] += size[pb]
            return True


        component = n
        
        for a,b in connections:
            if union(parents,a,b):
                component -= 1
        
        return component - 1

        

        