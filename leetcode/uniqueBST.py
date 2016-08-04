class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 1
        # the n+1 node can separate n node into 2 subtrees in all possible combination  
        # treeNum[i] stores number of possible combinations of i nodes
		treeNum = [0]*(n+1)
        treeNum[0],treeNum[1] = 1,1
        for i in range(2,n+1):
			# j is the number of left subtree, [0, i-1] 
			# then right subtree number is i-1-j
            for j in range(i):
                treeNum[i]+=treeNum[i-j-1]*treeNum[j]
                
        return treeNum[n]
