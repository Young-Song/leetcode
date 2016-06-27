class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <1 or n<1: return 0
        numOfPath = [ [0]*n for i in xrange(m)]
        
        for j in xrange(n):
            numOfPath[0][j]=1
        for i in xrange(m):
            numOfPath[i][0]=1
        # start from 1
		# if start from 0, index will be negative and the last few elements will be added     
        for i in xrange(1,m):
            for j in xrange(1,n):
                numOfPath[i][j]=numOfPath[i-1][j]+numOfPath[i][j-1]
                
        return numOfPath[m-1][n-1]
