#tc:O(nlogn) as we convert it to set in O(n) and the sort in O(nlogn)
#sc:O(n) as we are using a set
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        nums[:] = sorted(set(nums))
        return len(nums)



#tc: O(n) but sc: O(n) as we are using a hashmap to store the unique elements
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        seen = {}
        write_index = 0

        for num in nums:
            if num not in seen:
                seen[num] = True
                nums[write_index] = num
                write_index += 1

        return write_index