public class Solution {
    public boolean canJump(int[] nums) {
        if(nums==null||nums.length==0){
            return true;
        }
        int global_max = 0;
        for(int i=0;i<nums.length;i++){
            if(global_max<i){
                return false;
            }
            global_max = Math.max(global_max,nums[i]+i);
        }
        return global_max>=nums.length-1;
    }
}
