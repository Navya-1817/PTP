#tc:O(n) sc:O(1)

class Solution:
    def maxProfit(self, prices) -> int:
        l,r=0,1
        maxProf=0

        while r<len(prices):
            if prices[l]<prices[r]:
                prof=prices[r]-prices[l]
                maxProf=max(maxProf,prof)
            else:
                l=r
            r+=1
        return maxProf