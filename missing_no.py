class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        nums.sort()

        if nums[0] != 0:
            return 0

        if nums[-1] != n:
            return n

        for i in range(0, n - 1):
            j = nums[i] + 1
            if nums[i + 1] != j:
                return j
        return nums[-1]+1 