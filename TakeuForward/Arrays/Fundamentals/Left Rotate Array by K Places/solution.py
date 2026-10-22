class Solution:
    def rotateArray(self, nums, k: int) -> None:
        k %= len(nums)
        nums[:] = nums[k:] + nums[:k]