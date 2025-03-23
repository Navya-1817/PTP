#tc: O(n^2)
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)+1):
            t= target-nums[i]
            if t in nums and nums.index(t)!=i:
                return [i, nums.index(t)]
        return -1