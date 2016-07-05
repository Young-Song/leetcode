class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1:
            return s2==s3
        if not s2:
            return s1==s3
        if not s3:
            return False
        if len(s1)+len(s2)!= len(s3):
            return False
        m=len(s1)
        n=len(s2)
        l=len(s3)
        # dp[i][j]  :  up to i,j, s3[i+j-1] can be interleaved as s1[i-1] s2[j-1]
        dp = [[0]*(n+1) for i in range(m+1)]
        
        # "" can be interleaved as "" and ""
        dp[0][0]=True
        
        # initial conditions
        for j in range(1,n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1] 
        
        for i in range(1,m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
            
        # dp procedure 
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]= (dp[i-1][j] and s1[i-1]==s3[i+j-1] ) or ( dp[i][j-1] and s2[j-1]==s3[i+j-1])
        
        return dp[m][n]
