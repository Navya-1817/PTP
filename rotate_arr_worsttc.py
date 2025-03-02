class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums)-1
        while k>0:
            temp = nums[i]
            for j in range(i,0,-1):
                nums[j] = nums[j-1]
            nums[0] = temp
            k -= 1