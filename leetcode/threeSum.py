class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        elem = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            first = nums[i]
            left = i+1
            right=len(nums)-1
            while left < right:
                if first + nums[left]+nums[right]==0:
                    elem=[first,nums[left],nums[right]]
                    result.append(elem[:])
                    elem=[]
                    left+=1
                    right-=1
                    while left< right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                while(left<right and nums[left]+nums[right]+first<0 ):
                    left+=1
                while(left<right and nums[left]+nums[right]+first>0):
                    right-=1
               
        return result
            
        
        
