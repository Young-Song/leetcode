
class Solution(obejct):
	def rob(self):
		if nums == None or len(nums)== 0:
			return 0
		if len(nums) ==1:	
			return nums[0]
		n = len(nums)
		dp = [0]*n
		dp[0]=nums[0]
		dp[1]=max(dp[0],nums[1])
		for i in range(2,n):
			dp[i]=max(dp[i-2]+nums[i],dp[i-1])
		return dp[n-1]
