class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        
        # find left boundary and right boundary
        l_left=0
        l_right=len(nums)-1
        # l_left <= l_right not < because when they are equal we have to check the index 
        while l_left<=l_right:
            mid = (l_left+l_right)/2
            if nums[mid]==target:
                l_right=mid-1
            elif nums[mid]<target:
                l_left=mid+1
            else:
                l_right=mid-1
                
        r_left=0
        r_right=len(nums)-1
        
        while r_left<=r_right:
            mid = (r_left+r_right)/2
            if nums[mid] == target:
                r_left=mid+1
            elif nums[mid]< target:
                r_left=mid+1
            else:
                r_right=mid-1
        # l_left is the left bound of equal to target
        # r_right is the left bound of equal to target
        if r_right<l_left:
            return [-1,-1]
        return [l_left,r_right]
