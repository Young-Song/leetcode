public class Solution {
    public void moveZeroes(int[] nums) {
        if(nums==null||nums.length==0)
            return;
        int cur = 0;
        int non_zero=-1;
        int count=0;
        for(;cur<nums.length;cur++){
            if(nums[cur]!=0){
                nums[++non_zero]=nums[cur];
            }
            else{
                count++;
            }
        }

        while(count>0){
            nums[nums.length-count--]=0;
        }
        return ;
    }
}
