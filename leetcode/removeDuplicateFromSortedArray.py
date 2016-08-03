class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        uniqueTail = 0
        cur =1
        while cur<len(nums):
            if nums[uniqueTail]==nums[cur]:
                cur+=1
            else:
                uniqueTail+=1
                nums[uniqueTail]=nums[cur]
                cur+=1
        return uniqueTail+1
