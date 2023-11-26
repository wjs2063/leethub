
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # 1,5,3,9,8
        # 1,3,5,8,9
        # 0,2,2,1,1
        # 1,3,5,8,9
        n = len(nums)
        arr = [[nums[i],i] for i in range(n)]
        # nums[i] 가 작은순,인덱스 순으로 정렬 
        arr.sort()
        res = [0 for _ in range(n)]
        
        start = 0 
        
        while start < n :
            # 현재 시작지점 
            temp_start = start
            # 이다음 지점 
            end = temp_start + 1
            # index 에는 무엇을 담을래? 
            # 
            index = [arr[temp_start][1]]
            while end < n :
                if arr[end][0] - arr[temp_start][0] <= limit:
                    index.append(arr[end][1])
                    temp_start += 1
                    end += 1
                else:
                    break
            # 왜 소팅 ? 
            index.sort()
            for idx in index:
                res[idx] = arr[start][0]
                start += 1
        return res
            
            
                    
            
            
                
            
        
            
            
        
        