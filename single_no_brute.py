class Solution:
   def singleNumber(self, nums) -> int:
        nums.sort()
        n = len(nums)
        for i in range(0, n-1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]