"""this sol compares the original num to reversed num after converting 
the integer to string.
TC: O(n)
SC: O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = len(x)
        if (x[0:]==x[-1::-1]):
            return True
        else:
            return False