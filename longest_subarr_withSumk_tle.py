# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        n = len(arr)
        max_len = 0
    
        for i in range(n):
            for j in range(i, n):
                curr_sum = 0
                for m in range(i, j + 1):
                    curr_sum += arr[m]
                if curr_sum == k:
                    max_len = max(max_len, j - i + 1)
        
        return max_len