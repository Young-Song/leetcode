# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        prev = ListNode(0)
        newHead= prev
        prev.next=head
        
        cur = head
        while cur:
            if cur.val == val:
                prev.next= cur.next
                cur=cur.next
            else:
                prev=prev.next
                cur=cur.next
        
        return newHead.next
