class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums=sorted(nums)
        result = sys.maxint
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left < right:
                if nums[i]+nums[left]+nums[right]==target:
                    return target
                if abs(nums[i]+nums[left]+nums[right]-target)<abs(result-target):
                    result=nums[i]+nums[left]+nums[right]
                if  nums[i]+nums[left]+nums[right]<target:
                    left+=1
                elif nums[i]+nums[left]+nums[right]>target:
                    right-=1
                    
        return result
