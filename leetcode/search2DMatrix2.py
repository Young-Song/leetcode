class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)
        n = len(matrix[0])
        i=0
        j=n-1
        while i<m and j>=0:
            elem = matrix[i][j]
            if elem==target:
                return True
            elif elem<target:
                i+=1
            else:
                j-=1
        return False
        
