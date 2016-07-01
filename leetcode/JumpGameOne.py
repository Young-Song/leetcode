class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
            
        local_max =0
        global_max = 0
        for i in range(len(nums)):
            if global_max<i:
                return False
            local_max=max(i+nums[i],local_max)
            global_max= max(global_max,local_max)
            
        return global_max>=len(nums)-1
