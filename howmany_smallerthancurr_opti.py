#tc: o(nlogn) if we consider sort time else O(n)
#sc: o(n)

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        map = {}
        sorted_nums = sorted(nums)
        
        for i, num in enumerate(sorted_nums):
            if num not in map:  
                map[num] = i

        return [map[num] for num in nums]