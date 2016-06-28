class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        d ={}
        result =[]
        for idx,num in enumerate(nums):
            if target-num in d:
                result.append(d[target-num])
                result.append(idx)
            d[num]=idx
        return result
