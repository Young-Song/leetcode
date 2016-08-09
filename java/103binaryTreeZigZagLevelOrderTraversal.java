/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> elem = new ArrayList<Integer>();
        if(root==null){
            return result;
        }
        
        // a queue that keeps track of even-indexed list, left-to-right order
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        // a stack that keeps track of odd-indexed list, right-to-left order
        Stack<TreeNode> stack = new Stack<TreeNode>();
        // a stack that reverse the stack above so that the next level would be set correctly
        // without this stack, we can only access right most subtree at 2k+1, then we can't 
        // push the left-most node of 2k+2 (k>=1)
        Stack<TreeNode> reverse_stack = new Stack<TreeNode>();
        q.offer(root);
        // a mark of order
        int level = 0; 

        while(!q.isEmpty()|| !stack.isEmpty()){
            if(level%2==0){
                TreeNode top = q.poll();
                elem.add(top.val);
               
                if(top.left!=null){
                    stack.push(top.left);
                }
                if(top.right!=null){
                    stack.push(top.right);
                }
                //copy the list and clear
                //set the flag to stack
                if(q.isEmpty()){
                    result.add(new ArrayList<Integer>(elem));
                    elem.clear();
                    level+=1;
                }
            }
            else{
                //reverse the stack pushed by queue, 
                //we want the elements of this order
                //but we want the reverse order for next level, which is left-to-right
                while(!stack.isEmpty()){
                    TreeNode top = stack.pop();
                    elem.add(top.val);
                    reverse_stack.push(top);
                }
                //add reversed list onto result                
                result.add(new ArrayList<Integer>(elem));
                elem.clear();
                
                //push next level nodes in a left-to-right order
                while(!reverse_stack.isEmpty()){
                    TreeNode ordered_top = reverse_stack.pop();
                    if(ordered_top.left!=null)
                        q.offer(ordered_top.left);
                    if(ordered_top.right!=null)
                        q.offer(ordered_top.right);
                }
                level+=1;
            }
        } 
        return result;
    }
}
