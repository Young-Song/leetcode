class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = len(nums)/2
        count = 1
        elem = nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=elem :
                count-=1
            else:
                count+=1
            # since at most there are n/2 elements not equal to the majority 
            # once the count is negative the previous element can't be majority
            if count<0:
                count=1
                elem=nums[i]
        return elem
