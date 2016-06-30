class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        copy=nums[:]
        copy.extend(copy)
        start = len(nums)-k
        for i in range(len(nums)):
            nums[i]=copy[start+i]
            
        return 
