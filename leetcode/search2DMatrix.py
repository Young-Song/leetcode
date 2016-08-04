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
        left = 0
        right = m-1
        # when out of loop, l>r r is the row <= target
        while left<=right:
            mid = (left+right)/2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                left=mid+1
            else:
                right=mid-1
        row = right
        
        left=0
        right=n-1
        while left<=right:
            mid = (left+right)/2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
