class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        coor=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    coor.append((i,j))
                    
        for r,c in coor:
            for i in range(len(matrix)):
                matrix[i][c]=0
            for j in range(len(matrix[0])):
                matrix[r][j]=0
        
        
