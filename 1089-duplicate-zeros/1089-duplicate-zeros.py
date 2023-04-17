class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        idx = 0 
        while idx < n :
            if arr[idx] == 0 :
                arr.pop()
                arr.insert(idx,0)
                idx += 2
            else:
                idx += 1
        