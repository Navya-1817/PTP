#bruteforce approach --> TLE
#TC: O(n^2) SC: O(n)

class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                res.append(i)
        return res
    
#TC: O(n) SC: O(n)
def findDisappearedNumbers(self, nums):
        return list(set(range(1, len(nums)+1)) - set(nums))