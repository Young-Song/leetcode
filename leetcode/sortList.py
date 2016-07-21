# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # find middle node, odd or even, the second half is longer
        #helper = ListNode(0)
        #helper.next= head
        run =head
        walk = head
        prev = None
        while run and run.next:
            prev=walk
            walk = walk.next
            run = run.next.next
        if prev:
            prev.next= None
        first_half=self.sortList(head)
        second_half=self.sortList(walk)
        return self.merge_two_list(first_half,second_half)
    # Note that recursive merge_two_list may cause a maximum depth recursion error    
    def merge_two_list(self,l1, l2):
        helper = ListNode(0)
        hold=helper
        while l1 or l2:
            if not l1:
                helper.next= l2
                break
            if not l2:
                helper.next= l1
                break
            if l1.val<l2.val:
                helper.next=l1
                l1=l1.next
                helper=helper.next
            else:
                helper.next=l2
                l2=l2.next
                helper=helper.next
        return hold.next
