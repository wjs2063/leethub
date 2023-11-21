class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = int(1e9) + 7
        def rev(digit):
            return int(str(digit)[::-1])
        # rev 를 만족하는 순서쌍 개수 구하기 
        # easy solution
        """
        이중 for 문 후 만족 계산 -> N^2 * (logn) ^ 2 
        
        T(a + rev(b)) = T(b + rea(a))
        k = a - b == rev(a) - rev(b) -> 개수
        b = a - k 
        <-> 동치 
        k = nums[i] - rev(nums[i]) == nums[j] - rev(nums[j]) ->  i < j 
        
        -10^9 <= k <= 10^9
        0 <= a <= 10^9 흠 아닌가?
        k = rev(a) - rev(a - k) 찾는 등식과 같음 
        
        a != a - k -> k != 0 
        
        -1 = rev(a) - rev(a + 1)
        
        1 = rev(a) - rev(a - 1)
        2 = rev(a) - rev(a - 2)
        3 = rev(a) - rev(a - 3)
        
        abcd + hgfe == efgh + dcba 
        999(a - d) + 99(b - c) == 999(e - h) + 99(f - g)
        111(a - d - e + h) == 11( f - g + c -b)
        
        a - b -> dict 로 개수 
        
        dict[a] -> a 개수 
        rev_dict[a] -> 개수 
        abc - cba = 100a +10b + c - 100c -10b -a = 99a - 99c = 99*(a - c)
        abcd = 1000a + 100b + 10c + d = 1000d + 100c + 10b + a = 999a + 90b - 90c - 999d = 999(a - d) + 99(b - c)
        42 79 , 97 + 42 
        
        """
        
        rev_nums = [rev(num) for num in nums]
        
        arr = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            arr[i] = nums[i] - rev_nums[i]
        from collections import defaultdict
        # memo[v] := nums[i] - rev[i] 의 개수 
        memo = defaultdict(int)
        ans = 0
        for i,v in enumerate(arr):
            ans = (ans + memo[v]) % MOD
            # nums[1] - rev(nums[1]) 이있다고할때 memo 가 1증가한다.
            # 사실 이 한개만있어서는 정답에 추가될수없다 -> 2개쌍이 필요하기때문
            # 그다음번에 v라는 값이 나온다면 이전에 존재하던 memo[v] 값과 더해서 정답을 갱신하고 memo[v] 를 늘려준다.
            # arr[i] - rev(arr[i]) = 1 인게 3개정도 존재한다고 가정해보자 3C2 이므로  0,1,2 인덱스라고 가정하면 
            # arr[i] - rev(arr[i]) = 2인게 4개존재 -> 4C2 -> 6개 -> 1 + 2 + 3 
            # ''''''  = 3인게 6개 존재 -> 6C3 -> 1 + (1 + 2) + (1 + 2 + 3) + ( 1 + 2 + 3 + 4) -> 20 
            # 처음에 1이 더해지고 그이후에 2 가 더해짐 
            memo[v] += 1
        return ans
        
        
        # [n1,n2,n3,n4... nk]
        # [r1,r2,r3,r4..  rk]
        # n1 + rk = nk + r1 
        
        