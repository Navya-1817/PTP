#o(n^2) tc
#o(n) sc

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans = [0]*len(nums)
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            ans[i]=count
        return ans