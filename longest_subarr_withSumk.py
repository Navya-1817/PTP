# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        n = len(arr)
        map = {}
        sumo = 0
        max_len = 0
    
        for i in range(n):
            sumo += arr[i]
    
            if sumo == k:
                max_len = i + 1
    
            if (sumo - k) in map:
                max_len = max(max_len, i - map[sumo - k])
            
            if sumo not in map:
                map[sumo] = i
    
        return max_len