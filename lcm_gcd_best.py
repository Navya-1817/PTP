"""TC: O(log(min(a, b)))      SC: O(1)
this approach uses the Euclidean algorithm to find the gcd of a and b."""

class Solution:
    def lcmAndGcd(self, a : int, b : int):
        def gcd_calc(x, y):
            while y != 0:
                x, y = y, x % y
            return x
        
        gcd = gcd_calc(a, b)
        
        lcm = (a * b) // gcd
        
        return [lcm, gcd]