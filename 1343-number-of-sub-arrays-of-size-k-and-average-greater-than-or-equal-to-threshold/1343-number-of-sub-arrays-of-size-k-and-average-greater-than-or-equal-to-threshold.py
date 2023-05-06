from collections import deque
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k - 1])
        n = len(arr)
        res = 0
        for i in range(n - k + 1):
          s += arr[i + k - 1]

          if s >= k * threshold:
            res += 1
          s -= arr[i]
        return res
                


