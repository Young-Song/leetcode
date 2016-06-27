class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: 
            return 0
        m , n = len(grid),len(grid[0]) 
        minCost = [[0]*n for i in xrange(m)]
        minCost[0][0]= grid[0][0]
        for i in xrange(1,m): minCost[i][0]=minCost[i-1][0]+grid[i][0]
        for j in xrange(1,n): minCost[0][j]=minCost[0][j-1]+grid[0][j]
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                minCost[i][j]=min(minCost[i-1][j],minCost[i][j-1])+grid[i][j]
        
        return minCost[m-1][n-1]
