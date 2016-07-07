tion for singly-linked list.
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
        prev = head
        cur = prev.next
        n= None
        while cur:
            n = cur.next
            if prev.val == cur.val:
            	#set prev.next to next potential node
				#if cur is the last node we cannot modify prev in the
				#next iteration
				# SKIP duplicate 
				prev.next=cur.next
            else:
                prev.next=cur
                prev=cur
            cur=cur.next
        return head
        
