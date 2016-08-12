public class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums==null||nums.length==0)
            return 0;
        int tail =0;
        int cur=1;
        while(cur<nums.length){
            if(nums[cur]==nums[tail]){
                cur++;
            }
            else{
                nums[++tail]=nums[cur++];
            }
        }
        return tail+1;
    }
}
