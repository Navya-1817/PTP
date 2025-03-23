#tc: O(n^2)
#sc: O(1)

class Solution:
    def threeSum(self, nums):
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue

            j,k=i+1,len(nums)-1
            target = -nums[i]
            while(j<k):
                current_sum = nums[j]+nums[k]
                if(current_sum==target):
                    res.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif(current_sum<target):
                    j+=1
                else:
                    k-=1
        return res