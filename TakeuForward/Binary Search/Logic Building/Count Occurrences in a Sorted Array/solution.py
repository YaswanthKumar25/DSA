class Solution:
    def countOccurrences(self, arr: list[int], target: int) -> int:
        low = 0
        high = len(arr) - 1
        cnt = 0
        while low <= high:
            mid = (low + high) >> 1
            if arr[mid] == target:
                i = mid
                while i >= 0 and arr[i] == target:
                    cnt += 1
                    i -= 1
                j = mid + 1
                while j < len(arr) and arr[j] == target:
                    cnt += 1
                    j += 1
                return cnt
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1    
        return 0