class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        count = 0
        max_count = 0
    
        for j in range(0,len(nums)):
            if nums[j]==1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0

        return max(count, max_count)