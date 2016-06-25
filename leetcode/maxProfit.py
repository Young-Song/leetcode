class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # mins[i] keep track of min up to i-1
        # and keep maxProfit as the max diff between prices[i] and mins[i]
        if not prices:
            return 0
        mins = [0]*len(prices)
        mins[0]= sys.maxint
        maxProfit = 0
        for i in range(1,len(mins)):
            mins[i]=min(mins[i-1],prices[i-1])
            maxProfit =max(maxProfit,prices[i]-mins[i])
        return maxProfit
