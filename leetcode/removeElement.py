class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        tail = len(nums)-1# define: last elem index in the result
        idx = 0 # define: first elem index in the result
        while idx <= tail:
            if nums[idx]==val:
                nums[idx]=nums[tail] 
                tail-=1# removed one, length-1
            else:
                idx+=1

        return tail+1#len= index+1
