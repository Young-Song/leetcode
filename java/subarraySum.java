public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    public ArrayList<Integer> subarraySum(int[] nums) {
        // write your code here
        ArrayList<Integer> result = new ArrayList<Integer>();
        if(nums==null||nums.length==0){
            return result;
        }
        int sum =0;
        HashMap<Integer,Integer> hash = new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
            if(nums[i]==0){
                result.add(i);
                result.add(i);
                break;//found
            }
            if(hash.containsKey(sum)){
                result.add(hash.get(sum)+1);
                result.add(i);
                break;
            }
            if(sum==0){
                result.add(0);
                result.add(i);
                break;
            }
            hash.put(sum,i);
        }
        return result;
    }
}
