class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        nums1,nums2=sorted(nums1),sorted(nums2)
        
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
            
        for i in range(len(nums1)):
            if i>0 and nums1[i]==nums1[i-1]:
                continue
            if self.binSearch(nums2,0,len(nums2)-1,nums1[i]):
                result.append(nums1[i])
            else:
                continue
            
        return result
        
        
    def binSearch(self,nums,left,right,target):
        if left>right:
            return False
        mid = (left+right)/2
        if nums[mid]==target:
            return True
        elif nums[mid]<target:
            return self.binSearch(nums,mid+1,right,target)
        else:
            return self.binSearch(nums,left,mid-1,target)
        
