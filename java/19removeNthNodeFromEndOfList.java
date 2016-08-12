/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head==null||head.next==null)
            return null;
        ListNode cur = head;
        while(cur!=null && n>0){
            cur=cur.next;
            n--;
        }
        if(cur==null){
            return head.next;
        }
        
        ListNode walk= head;
        while(cur.next!=null){
            walk=walk.next;
            cur=cur.next;
        }
        
        walk.next=walk.next.next;
        return head;
    }
}
