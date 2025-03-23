#Time complexity: O(n log n) 
#Space complexity: O(n)

class Solution:
    def sortedSquares(self, nums):
        arr = []
        for num in nums:
            arr.append(num**2)
        return sorted(arr)