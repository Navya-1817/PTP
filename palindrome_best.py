"""This approach is similar to the previous one, 
but instead of reversing the entire string, 
we reverse the first half of the integer.
TC: O(log(n))
SC: O(1)"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): 
            return False
        
        rev_half = 0
        while x > rev_half:
            rev_half = rev_half * 10 + x % 10
            x //= 10
     
        return x == rev_half or x == rev_half // 10