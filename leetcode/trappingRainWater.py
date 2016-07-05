class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = [0]*len(height)
        right_max = [0]*len(height)
        max_value = 0
        for i in range(1,len(height)):
            max_value = max(height[i-1],max_value)
            left_max[i] = max_value
            
        # reset max value
        max_value =0 
        for i in reversed(range(len(height)-1)):
            max_value = max(height[i+1],max_value)
            right_max[i] = max_value
            
        result =[0]*len(height)
        for i in range(len(height)):
            if min(left_max[i],right_max[i])-height[i] > 0:
                result[i] = min(left_max[i],right_max[i])-height[i]
        return sum(result)
