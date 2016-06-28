class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0]*len(nums)
        dp[0]=1
        for i in range(1,len(nums)):
            max_len = 1
            for j in range(i):
                if nums[j]<nums[i]:
                    max_len=max(max_len,dp[j]+1)
            dp[i]=max_len
        # note that dp[i] indicates the lis ending at i
        # therefore, we need to find the max in dp.
        # NOT dp[-1]
        return max(dp)
