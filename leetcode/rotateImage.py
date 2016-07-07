class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return 
        n = len(matrix)
        level = n/2
        # rotate by level
		# for each level, swap the array in a non-overlapping way
		
        for l in range(level):
            for j in range(l,n-1-l):
                temp=matrix[l][j]
                matrix[l][j]=matrix[n-1-j][l]
                matrix[n-1-j][l]=matrix[n-1-l][n-1-j]
                matrix[n-1-l][n-1-j]=matrix[j][n-1-l]
                matrix[j][n-1-l]=temp
                
