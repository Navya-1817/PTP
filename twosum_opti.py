#O(n) tc and sc

class Solution:
    def twoSum(self, nums, target: int):
        mapo = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapo:
                return [mapo[diff], i]
            mapo[n]=i