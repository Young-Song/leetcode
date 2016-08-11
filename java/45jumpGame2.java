public class Solution {
    public int jump(int[] nums) {
        int i = 0;
        int step = 0;
        if(nums.length==1){
            return 0;
        }

        while(i<nums.length){
            if(nums[i]+i>=nums.length-1){
                step++;
                break;
            }

            int next_max=0;
            int next_index=i+1;
            for(int j=i+1;j<=nums[i]+i && j<nums.length;j++){
                if(next_max<nums[j]+j){
                    next_max=nums[j]+j;
                    next_index=j;
                }
            }
            i=next_index;
            step+=1;
        }
        
        return step;
    }
}
