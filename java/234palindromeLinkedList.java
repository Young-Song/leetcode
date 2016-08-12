/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head==null||head.next==null)
            return true;
        ListNode run = head;
        ListNode walk = head;
        while(run.next!=null && run.next.next!=null){
            run=run.next.next;
            walk=walk.next;
        }
        
        ListNode cur2 = walk.next;
        walk.next=null;
        
        ListNode prev = null;
        ListNode next = null;
        while(cur2!=null){
            next=cur2.next;
            cur2.next=prev;
            prev=cur2;
            cur2=next;
        }
        ListNode cur=head;
        while(prev!=null){
            if(prev.val!=cur.val){
                return false;
            }
            prev=prev.next;
            cur=cur.next;
        }
        
        return true;
    }
}
