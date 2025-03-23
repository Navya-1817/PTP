#O(n) tc and O(1) sc

class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        
        ans = 0
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            target_x, target_y = points[i + 1]
            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
            
        return ans