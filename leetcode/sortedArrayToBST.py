# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildTree(nums,0,len(nums)-1)
        
    def buildTree(self,nums,left,right):
        if left>right:
            return None
        mid = (left+right)/2
        root = TreeNode(nums[mid])
        root.left = self.buildTree(nums,left,mid-1)
        root.right=self.buildTree(nums,mid+1,right)
        return root
