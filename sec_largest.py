class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n < 2:
            return None  # Not enough elements to have a second largest

        maxo = float('-inf')
        sec_max = float('-inf')

        for i in range(n):
            if arr[i] > maxo:
                sec_max = maxo
                maxo = arr[i]
            elif arr[i] > sec_max and arr[i] != maxo:
                sec_max = arr[i]

        return sec_max if sec_max != float('-inf') else -1