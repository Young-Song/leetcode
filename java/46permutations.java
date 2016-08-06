public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> elem = new ArrayList<Integer>();
        if(nums==null||nums.length==0)
            return result;
        boolean[] used = new boolean[nums.length];
        backtrack(nums,used,result,elem);
        return result;
    }
    
    public void backtrack(int[] nums, boolean[] used,List<List<Integer>> result, List<Integer> elem){
        if(elem.size()==nums.length){
            result.add(new ArrayList<Integer>(elem));
            return ;
        }
        
        for(int i=0;i<nums.length;i++){
            if(!used[i]){
                elem.add(nums[i]);
                used[i]=true;
                backtrack(nums,used,result,elem);
                elem.remove(elem.size()-1);
                used[i]=false;
            }
        }
    }
}
