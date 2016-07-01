class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        buf = []
        self.helper(n,k,result,buf,1)
        return result
        
    def helper(self,n,k,result,buf,start):
        if not k:
            result.append(buf[:])
            return 
        for i in xrange(start,n+1):
            buf.append(i)
            self.helper(n,k-1,result,buf,i+1)
            del buf[-1]
