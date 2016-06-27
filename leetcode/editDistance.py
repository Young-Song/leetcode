class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
            
        m = len(word1)
        n = len(word2)
        dist = [[0]*(n+1) for i in range(m+1)]
        
        # construct a substring up to index i if word1(or j of word2) from an empty string ""
        for i in range(m+1):
            dist[i][0]=i
        for j in range(n+1):
            dist[0][j]=j
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                # dist has an extra empty in the beginning so index-1 for string index
                if word1[i-1] == word2[j-1]:
                    dist[i][j]=dist[i-1][j-1]
                else:# not equal
                    minDist = min(dist[i-1][j-1],dist[i-1][j])
                    minDist = min(minDist, dist[i][j-1])
                    dist[i][j] = minDist+1
        return dist[m][n]
        
