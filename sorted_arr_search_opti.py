#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        l, r = 0, len(arr)-1
        while(l<=r):
            mid = l + (r-l)//2
            if arr[mid]==k:
                return True
            elif arr[mid]<k:
                l = mid+1
            else:
                r = mid-1
        return False