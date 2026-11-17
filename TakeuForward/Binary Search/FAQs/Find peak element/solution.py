class Solution:
    def findPeakElement(self, arr):
        if len(arr) == 1:
            return 0
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) >> 1
            if mid == 0:
                if arr[0] > arr[1]:
                    return 0
                else:
                    low = mid + 1
                    continue
            if mid == len(arr) - 1:
                if arr[-1] > arr[-2]:
                    return mid
                else:
                    high = mid - 1
                    continue
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
