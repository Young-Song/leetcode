class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums)<2:
            return False
        return len(set(nums))!=len(nums)
