#optimised code for returning the sum of the digits of a number that divide it

class Solution:
    def evenlyDivides(self, n):
        # code here
        count = 0
        num = n
        while (n>0):
            r = n%10
            if (r!=0 and num%r==0):
                count += 1
            n = n//10
        return count