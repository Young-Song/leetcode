class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left = 0
        right = len(height)-1
        maxWater = 0
        while left<=right:
            maxWater = max(min(height[left],height[right])*(right-left), maxWater)
            if height[left]<= height[right]:
                left+=1
            else:
                right-=1
        return maxWater
        
