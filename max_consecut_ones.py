class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max_count = 0
    
        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] == 1:
                    count += 1
                    max_count = max(max_count, count)
                else:
                    break
        
        return max_count