class Solution(object):
    def minPathSum(self, grid):
        rows=len(grid)
        columns=len(grid[0])
        for i in range(1,columns):
            grid[0][i]+=grid[0][i-1]
        for j in range(1,rows):
            grid[j][0]+=grid[j-1][0]
        for i in range(1,rows):
            for j in range(1,columns):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[rows-1][columns-1]