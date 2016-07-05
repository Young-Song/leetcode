class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix)==0 or len(matrix[0])==0:
            self.sum = []
            return 
        m = len(matrix)
        n = len(matrix[0])
        # set a sum matrix to store the sum at i,j. not matrix values
        self.sum = [[0]*(n+1) for i in range(m+1)]
        
        #sum[i][j] : sum up to matrix[i-1][j-1] 
        for i in range(1,m+1):
            self.sum[i][0]=self.sum[i-1][0]+matrix[i-1][0]
        for j in range(1,n+1):
            self.sum[0][j]=self.sum[0][j-1]+matrix[0][j-1]

        for i in range(1,m+1):
            for j in range(1,n+1):
                self.sum[i][j]=self.sum[i-1][j]+self.sum[i][j-1]-self.sum[i-1][j-1]+matrix[i-1][j-1]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # general case
        return self.sum[row2+1][col2+1] - self.sum[row1][col2+1]-self.sum[row2+1][col1]+self.sum[row1][col1]
        
        
# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
