public class Solution {
    public int majorityElement(int[] nums) {
        if(nums==null||nums.length==0){
            return 0;
        }
        int candidate = nums[0];
        int count = 1;
        for(int i=1;i<nums.length;i++){
            if(nums[i]!=candidate){
                count--;
            }
            else{
                count++;
            }
            if(count==0){
                candidate=nums[i];
                count=1;
            }
        }
        return candidate;
    }
}
