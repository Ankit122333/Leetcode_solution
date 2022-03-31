class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]<0):
                    count+=1
        return count
        