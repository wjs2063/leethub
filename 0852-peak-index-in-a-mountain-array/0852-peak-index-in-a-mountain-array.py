class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        sn, en = 1, len(arr) - 2
        
        while sn <= en :
            mid = (sn + en) // 2
            if arr[mid -1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1 ] < arr[mid] < arr[mid + 1]:
                sn = mid + 1
            else:
                en = mid - 1
        