class Solution:
   def singleNumber(self, nums) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res