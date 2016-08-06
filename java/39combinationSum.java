public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> candidate = new ArrayList<Integer>();
        if(candidates==null||candidates.length==0){
            return result;
        }
        //sort the array so that when sum exceeds target, we can stop
        Arrays.sort(candidates);
        findSum(candidates,target,result,candidate,0);
        return result;
    }
    
    public void findSum(int[] candidates, int target, List<List<Integer>> result, List<Integer> candidate, int idx){
        // a list suming up to target is found
        if(target==0){
            result.add(new ArrayList<Integer>(candidate));
            return;
        }
        // the list sum exceeds target 
        if(target<0){
            return;
        }
        for(int i=idx;i<candidates.length;i++){
            candidate.add(candidates[i]);
            //note that a number can be used unlimited times, so we pass i, not i+1
            findSum(candidates,target-candidates[i],result,candidate,i);
            candidate.remove(candidate.size()-1);
        }
    }
}
