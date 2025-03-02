class Solution:
    def largest(self, arr):
        # code here
        maxo = arr[0]
        for i in arr:
            if i>maxo:
                maxo = i
        return maxo