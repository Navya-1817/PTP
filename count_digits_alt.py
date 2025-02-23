#alternative methods but not efficient

class Solution:
    def evenlyDivides(self, n):
        num_str = str(n)
        num = int(num_str)
        
        count = sum(1 for digit in num_str if int(digit) != 0 and num % int(digit) == 0)
        
        return count



class Solution:
    def evenlyDivides(self, n, num=None):
        if num is None:
            num = n
        
        if n == 0:
            return 0
        
        digit = n % 10
        count = 1 if digit != 0 and num % digit == 0 else 0
        
        return count + self.evenlyDivides(n // 10, num)
