# tc: O(n*m) and sc: O(n*m)

class Solution:
    def spiralOrder(self, matrix):
        i,j = len(matrix), len(matrix[0])
        u, d, l, r = 0, i-1, 0, j-1
        ans = []

        while len(ans)<i*j:
            for k in range(l, r+1):
                ans.append(matrix[u][k])
            u +=1

            for k in range(u, d+1):
                ans.append(matrix[k][r])
            r -= 1

            if u<=d:
                for k in range(r, l-1, -1):
                    ans.append(matrix[d][k])
                d -= 1

            if l<=r:
                for k in range(d, u-1, -1):
                    ans.append(matrix[k][l])
                l += 1

        return ans
