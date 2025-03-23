#tc: O(n * max(dx, dy)) where dx is the maximum value of |x2 - x1| and dy is the maximum value of |y2 - y1|
#sc: O(1)

class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        
        ans = 0
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            target_x, target_y = points[i + 1]
            
            while curr_x != target_x or curr_y != target_y:
                if curr_x < target_x:  
                    curr_x += 1  
                elif curr_x > target_x:
                    curr_x -= 1  

                if curr_y < target_y:
                    curr_y += 1  
                elif curr_y > target_y:
                    curr_y -= 1  

                ans += 1  
            
        return ans