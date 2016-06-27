class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return nums[0]
            
        local_max=-sys.maxint-1
        global_max=local_max
        for num in nums:
            
            local_max= max(local_max+num,num)
                
            global_max=max(global_max,local_max)
            
        return global_max
