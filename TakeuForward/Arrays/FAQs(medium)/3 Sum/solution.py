class Solution:
    def threeSum(self, nums: list) -> list[list]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return [list(t) for t in set(tuple(triplet) for triplet in ans)]
