public class Solution {
    public int maxSubArray(int[] nums) {
        // at least one number
        int globalMax =Integer.MIN_VALUE;
        int localMax = 0;//before i 
        for(int i=0;i<nums.length;i++){
            localMax = Math.max(nums[i],localMax+nums[i]);
            globalMax = Math.max(globalMax,localMax);
        }
        
        return globalMax;
    }
}
