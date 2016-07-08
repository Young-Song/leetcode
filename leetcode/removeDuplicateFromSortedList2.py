# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # helper node
        p = ListNode(0)
        helper = p
        p.next= head
        cur = head
        
        while cur and cur.next:
            # duplicate
            if cur.val==cur.next.val:
                dup = cur.val
                while cur and cur.val==dup:
                    cur=cur.next
                
                # when out of the above loop, cur is either None or next node of a different val
                p.next= cur
            # unique 
            else:
                p.next=cur
                p=p.next
                cur=cur.next
                
        return helper.next
        
