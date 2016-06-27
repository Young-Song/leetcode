class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        numPath = [[0]*n for i in xrange(m)]
        numPath[0][0]=1-obstacleGrid[0][0]
        for i in xrange(1,m):
            if numPath[i-1][0]==0 or obstacleGrid[i][0]==1:
                numPath[i][0]=0
            else:
                numPath[i][0]=1
        for j in xrange(1,n):
            if numPath[0][j-1]==0 or obstacleGrid[0][j]==1:
                numPath[0][j]=0
            else:
                numPath[0][j]=1
                
        for i in xrange(1,m):
            for j in xrange(1,n):
                if obstacleGrid[i][j] != 1:
                    numPath[i][j] = numPath[i-1][j]+numPath[i][j-1]
                    
        return numPath[m-1][n-1]
        
