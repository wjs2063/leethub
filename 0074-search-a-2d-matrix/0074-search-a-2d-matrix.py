class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        from bisect import bisect_left
        n = len(matrix)
        m = len(matrix[0])
        l,r = 0, n * m - 1

        while l <= r :
            mid = (l + r) // 2

            if target < matrix[mid // m][mid % m]:
                r = mid - 1
            elif target == matrix[mid // m][mid % m]:
                return True
            else:
                l = mid + 1
        return False
 