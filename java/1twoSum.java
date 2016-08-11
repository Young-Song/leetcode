public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        if(nums==null||nums.length==0){
            return result;
        }
        
        HashMap<Integer,Integer> hash = new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            if(hash.containsKey(nums[i])){
                result[0]=hash.get(nums[i]);
                result[1]=i;
                break;
            }
            hash.put(target-nums[i],i);
        }
        return result;
    }
}
