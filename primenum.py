#iterates through all nums in the range and thus is less efficient

class Solution:
    def isPrime(self, x: int) -> bool: 
        if x < 2:
            return False
           
        for i in range(2, x):  
            if x % i == 0:
                return False
        
        return True