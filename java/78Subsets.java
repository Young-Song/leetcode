public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> elem = new ArrayList<Integer>();
        if(nums==null||nums.length==0){
            return result;
        }
        result.add(new ArrayList<Integer>());
        generateSubsets(nums,result,elem,0);
        return result;
    }
    
    public void generateSubsets(int[] nums, List<List<Integer>> result, List<Integer> elem,int idx){
        if(elem.size()>nums.length){
            return;
        }
        
        for(int i=idx;i<nums.length;i++){
            elem.add(nums[i]);
            result.add(new ArrayList<Integer>(elem));
            generateSubsets(nums,result,elem,i+1);
            elem.remove(elem.size()-1);
        }
        
    }
}
