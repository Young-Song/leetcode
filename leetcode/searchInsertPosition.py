class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        left=0
        right=len(nums)-1
        while left<=right:
            mid = (left+right)/2
            if target>nums[mid]:
                left=mid+1
            elif target==nums[mid]:
                right=mid-1
            else:
                right=mid-1
        return left
        
