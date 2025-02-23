#O(n^2) time complexity and leads to TLE

class Solution:
    def sumOfDivisors(self, n):
        # Helper function to calculate sum of divisors of a number
        def func(num):
            fac_sum = 0
            for j in range(1, num + 1):
                if num % j == 0:
                    fac_sum += j
            return fac_sum

        sumo = 0
        for i in range(1, n + 1):
            sumo += func(i)
        
        return sumo
