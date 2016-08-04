class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        count=0
        visited = [[False]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                # if a '1' (land) is unvisted, run DFS on it, increment the count
                if not visited[i][j] and grid[i][j]=='1':
                    count+=1
                    self.markIslands(grid, visited, i, j)
        return count 


    def markIslands(self, grid, visited, i, j):
        if visited[i][j] or grid[i][j]=='0':
            return
        m = len(grid)
        n = len(grid[0])
        
        # set 1 to be visited 
        visited[i][j]=True
        if j>0:
            self.markIslands(grid,visited,i,j-1)
        if j<n-1:
            self.markIslands(grid,visited,i,j+1)
        if i>0:
            self.markIslands(grid,visited,i-1,j)
        if i<m-1:
            self.markIslands(grid,visited,i+1,j)
