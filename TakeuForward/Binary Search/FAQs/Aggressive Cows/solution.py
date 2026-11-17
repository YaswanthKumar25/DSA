class Solution:
    def aggressiveCows(self, nums: list[int], k: int) -> int:
        nums.sort()
        low = 1
        high = nums[-1] - nums[0]
        while low <= high:
            mid = (low + high) >> 1
            if self.can_place_cows(nums, mid, k):
                low = mid + 1
            else:
                high = mid - 1
        return high

    def can_place_cows(self, stalls, min_dist, k):
        cows_placed = 1
        last_pos = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= min_dist:
                cows_placed += 1
                last_pos = stalls[i]
                if cows_placed == k:
                    return True
                    
        return False
