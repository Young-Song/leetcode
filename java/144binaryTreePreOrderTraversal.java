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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if(root==null){
            return result;
        }
        Stack<TreeNode> s = new Stack<TreeNode>();
        TreeNode cur = root;
        //s.push(cur);
        
        while(!s.isEmpty()||cur!=null){
            if(cur!=null){
                result.add(cur.val);
                s.push(cur);
                cur=cur.left;
            }
            else{
                TreeNode top = s.pop();
                cur=top.right;
            }
        }
        return result;
    }
}
