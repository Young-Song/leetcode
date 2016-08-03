# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return 
        q= deque([])
        cur = root
        q.append(cur)
        cur_level=1# cur already pushed into Queue 
        next_level=0
        while q:
            top = q.popleft()
            if q:
                top.next=q[0]
            else:
                top.next=None
            cur_level-=1
            if top.left:
                q.append(top.left)
                next_level+=1
            if top.right:
                q.append(top.right)
                next_level+=1
            # cut the list and point to null
            if cur_level==0:
                top.next= None
                cur_level=next_level
                next_level=0
            
