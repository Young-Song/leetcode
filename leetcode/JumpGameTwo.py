class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_reach = 0
        reach = 0
        min_step =0
        for i in range(len(nums)):
            if i> last_reach :
                min_step+=1
                last_reach =reach
            reach = max(reach, nums[i]+i)
            
        return min_step
        
