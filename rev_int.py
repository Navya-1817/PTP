class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0]!='-':
            x = x[::-1]
        else:
            x = x[0] + x[-1:0:-1]
        x = int(x)
        if (abs(x)<2**31 and x!= 2**31-1):
            return x  
        return 0