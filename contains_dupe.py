#tc: O(n)
#sc: O(n)

class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(set(nums)) != len(nums)