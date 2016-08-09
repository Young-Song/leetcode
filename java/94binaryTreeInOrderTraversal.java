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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if(root==null){
            return result;
        }
        
        Stack<TreeNode> s = new Stack<TreeNode>();
        TreeNode cur = root;
        while(!s.isEmpty()||cur!=null){
            if(cur!=null){
                s.push(cur);
                cur=cur.left;
            }
            else{
                TreeNode top = s.pop();
                result.add(top.val);
                cur=top.right;
            }
            
        }
        
        return result;
    }
}
