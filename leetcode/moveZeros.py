class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tail = 0
        for num in range(len(nums)):
            if nums[num]:# not equal = 0
                nums[tail], nums[num] = nums[num],nums[tail]
                tail+=1
        
