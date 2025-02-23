#O(√x) time complexity and O(1) space complexity

class Solution:
    def isPrime(self, x: int) -> bool:
        if x < 2:
            return False
        if x == 2:
            return True  # 2 is the only even prime number
        if x % 2 == 0:
            return False  # Skip all other even numbers
        
        for i in range(3, int(x ** 0.5) + 1, 2):  # Check only odd numbers
            if x % i == 0:
                return False
        
        return True