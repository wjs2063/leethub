class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        1 2 3 4 ... 10 (2k + 1)
        2 4 6 8 10 
        2 * [1,2,3,4,5]
        2 * [1 2 3 4] -> 2 * [1 2 .. k]
        """
        def sol(n : int,step : int):
            if n == 1 :return 1 
            if n % 2 == 0:
                if step % 2 == 0 :
                    return 2 * sol(n // 2, step + 1)
                else:
                    return 2 * sol(n // 2,step + 1) - 1

            else:
                if step % 2 == 0:
                    return 2 * sol(n // 2,step + 1)
                else:
                    return 2 * sol(n // 2,step + 1)
        return sol(n,0)
