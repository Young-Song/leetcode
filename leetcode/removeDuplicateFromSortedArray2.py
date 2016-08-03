class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        tail = 1
        for i in range(2,len(nums)):
            if nums[i]!=nums[tail]:
                tail+=1
                nums[tail]=nums[i]
            else:
                if nums[tail]==nums[tail-1]:
                    continue
                else:
                    tail+=1
                    nums[tail]=nums[i]
        return tail+1
