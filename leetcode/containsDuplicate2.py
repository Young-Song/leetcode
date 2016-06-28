class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i,elem in enumerate(nums):
            if elem in d:
                if i-d[elem]<=k:
                    return True
            d[elem]=i
        return False
