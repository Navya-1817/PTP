#O(n) time complexity 

class Solution:
    def sumOfDivisors(self, n):
        sumo = 0
        for i in range(1, n + 1):
            sumo += i * (n // i)  # Contribution of i to all its multiples
        return sumo