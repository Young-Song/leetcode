class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        count = 1 
        m = len(matrix)
        n = len(matrix[0])
        MinLevelNum= min(m,n)
        MinLevel = MinLevelNum/2
        result = []
        
        for level in range(MinLevel):
            for j in range(level,n-1-level):
                result.append(matrix[level][j])
                
            for i in range(level,m-1-level):
                result.append(matrix[i][n-1-level])
            # compared with first level in row, shift down by 1    
            for j in reversed(range(level+1, n-level)):
                result.append(matrix[m-1-level][j])
            # compared with first level in col, shift right by 1    
            for i in reversed(range(level+1, m-level)):
                result.append(matrix[i][level])
        # Compare Min(row,col) NOTE not the level number( which is even because levelnum = min/2)
        if MinLevelNum%2 ==1: # odd minimum levels -- one extra row/column to fill
            if m<n:
                # index starts at MinLevel, ends at n-1-MinLevel+1
                for j in range(MinLevel,n-MinLevel):
                    result.append(matrix[MinLevel][j])
            else:
                # index starts at MinLevel, ends at m-1-MinLevel+1
                for i in range(MinLevel,m-MinLevel):
                    result.append(matrix[i][MinLevel])
        return result
                
