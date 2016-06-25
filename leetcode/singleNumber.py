class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for num in nums:
            single = single ^ num
        return single
