#tle
#tc:O(n^2) sc:O(1)

class Solution:
    def maxProfit(self, prices) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return res