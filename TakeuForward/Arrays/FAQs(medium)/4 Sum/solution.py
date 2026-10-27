class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            for l in range(i+1,len(nums)):
                j = l + 1
                k = len(nums) - 1
                while j < k:
                    if nums[i] +nums[l]+ nums[j] + nums[k] == target:
                        ans.append([nums[i],nums[l], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif nums[i] +nums[l]+ nums[j] + nums[k] > target:
                        k -= 1
                    else:
                        j += 1
        return [list(t) for t in set(tuple(triplet) for triplet in ans)]
