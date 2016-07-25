# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque([])
        cur_level = 1
        next_level=0
        q.append(root)
        result=[]
        elem=[]
        while len(q)!=0:
            top = q.popleft()
            cur_level-=1
            elem.append(top.val)
            if top.left:
                q.append(top.left)
                next_level+=1
            if top.right:
                q.append(top.right)
                next_level+=1
            if cur_level==0:
                result.append(elem)
                cur_level=next_level
                next_level=0
                elem=[]
        # bottom-up
        # NOTE: reverse() reverse the list in place, and returns None
        # e.x. result = resule.reverse() will assign None to result
        result.reverse()
        return result
