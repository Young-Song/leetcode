class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        # linear initialization
        self.sum = [0]*(len(nums)+1)
        for i in range(1,len(self.sum)):
            self.sum[i]=self.sum[i-1]+nums[i-1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        # constant query
        return self.sum[j+1]-self.sum[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
