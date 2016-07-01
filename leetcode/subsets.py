class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[[]]
        buf=[]
        self.helper(nums,result,buf,0)
        return result
        
    def helper(self,nums,result,buf,idx):
        
        for i in range(idx,len(nums)):
            buf.append(nums[i])
            result.append(buf[:])
            self.helper(nums,result,buf,i+1)
            def buf[-1]        
