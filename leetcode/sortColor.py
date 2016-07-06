class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r=0
        w=0
        b=0
        for num in nums:
            if num==0:
                r+=1
            elif num==1:
                w+=1
            else:
                b+=1
        for i in range(len(nums)):
            if i<r:
                nums[i]=0
            elif i<r+w:
                nums[i]=1
            else:
                nums[i]=2
                
                
