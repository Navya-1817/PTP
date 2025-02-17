"""TC: O(max(a,b))      SC: O(1)
a and b are divided with all nums from 2 to max(a,b), until the gcd is found. 
lcm is then found usinng a formula. not the best approach"""

class Solution:
    def lcmAndGcd(self, a : int, b : int):
        gcd = 1
        for i in range(2,max(a,b)):
            if a%i==0 and b%i==0:
                gcd = i
        lcm = (a*b)//gcd
        return [lcm, gcd]