class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
		# add duplicate as many time as it appears in both arrays
        result=[]
        nums1,nums2=sorted(nums1),sorted(nums2)
        n1,n2=0,0
        while n1<len(nums1) and n2<len(nums2):
            if nums1[n1]<nums2[n2]:
                n1+=1
            elif nums1[n1]>nums2[n2]:
                n2+=1
            else:
                result.append(nums1[n1])
                n1+=1
                n2+=1
        return result
        
