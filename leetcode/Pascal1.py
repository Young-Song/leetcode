class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows ==0:
            return []
        result = []
        result.append([1])
        for i in range(1,numRows):
            result.append([1]*(i+1))
            for j in range(1,i):
                result[i][j]=result[i-1][j]+result[i-1][j-1]
        return result
