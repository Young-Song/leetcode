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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> elem = new ArrayList<Integer>();
        if(root==null){
            return result;
        }
        
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int cur_level=1;
        int next_level=0;
        while(!q.isEmpty()){
            TreeNode top = q.poll();
            elem.add(top.val);
            cur_level-=1;
            if(top.left!=null){
                q.offer(top.left);
                next_level+=1;
            }
            if(top.right!=null){
                q.offer(top.right);
                next_level+=1;
            }
            if(cur_level==0){
                result.add(new ArrayList<Integer>(elem));
                cur_level=next_level;
                next_level=0;
                elem.clear();
            }
        }

        return result;
    }
}
