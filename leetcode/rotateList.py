# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head or k==0:
            return head
        size = 0
        cur = head
        prev =None
        while cur:
            prev=cur
            cur=cur.next
            size+=1
        # k might be greater than size
        k=k%size
        # make it circular
        prev.next = head
        ret = head
        iter = size-k
        while iter>0:
            prev=ret
            ret=ret.next
            iter-=1
        prev.next=None
        return ret
