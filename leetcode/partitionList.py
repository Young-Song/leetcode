# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        smaller = ListNode(0)
        newHead = smaller
        greater = ListNode(0)
        newMiddle = greater
        
        cur = head
        while cur :
            if cur.val < x:
                smaller.next= cur
                smaller = smaller.next
                cur=cur.next
                # set next to none
                smaller.next=None
            else:
                greater.next = cur
                greater= greater.next
                cur=cur.next
                # set next to none
                greater.next= None
                
        smaller.next= newMiddle.next
        return newHead.next
