class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        minCoin =[sys.maxint]*(amount+1)
        minCoin[0]=0
        for i in xrange(1,amount+1):
            minCount = sys.maxint
            for c in coins:
                if i-c>=0 and minCount> minCoin[i-c]:
                    minCount=minCoin[i-c]+1
            minCoin[i]=minCount# update min number of coins at i
        # if the last element is max, we can make change with coins given
        return minCoin[amount] if minCoin[amount]!=sys.maxint else -1
