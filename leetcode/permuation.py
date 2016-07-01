class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        buf = []
        used = [False]*len(nums)
        self.helper(nums,used,result,buf)
        return result
        
    def helper(self,nums,used,result,buf):
        # if index == len(nums) => subsets
        if len(buf)==len(nums):
            result.append(buf[:])
            return 
        for i in range(len(nums)):
            if not used[i]:
                buf.append(nums[i])
                used[i]=True
                self.helper(nums,used,result,buf)
                used[i]=False
                del buf[-1]
        
