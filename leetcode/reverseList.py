# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        prev = None
        cur =head
        n= None
        while cur:
            n = cur.next
            cur.next=prev
            prev=cur
            cur=n
        return prev
