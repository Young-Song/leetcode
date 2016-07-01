class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.binSearch(nums,0,len(nums)-1)
        
    def binSearch(self,nums,left,right):
        if left==right:
            return nums[left]
        mid = (left+right)/2
        if nums[left]<=nums[mid]<nums[right]:
            return nums[left]
        elif nums[mid]<nums[right]<nums[left]:
            return self.binSearch(nums,left,mid)
        else:
            return self.binSearch(nums,mid+1,right)
