public class Solution {
    public int lengthOfLIS(int[] nums) {
        if(nums==null||nums.length==0){
            return 0;
        }
        //dp array that stores max_lis ending at i
        int[] lis = new int[nums.length];
        lis[0]= 1;
        
        // a global max that stores max lis of the entire array
        int global_max = 1;
        for(int i=1;i<nums.length;i++){
            int local_max = 1;
            for(int j=i-1;j>=0;j--){
                //for all elements lis[j] which is less than lis[i], find the max lis ending at j
                if(nums[j]<nums[i]){
                    local_max=Math.max(lis[j]+1,local_max);
                }
            }
            lis[i]=local_max;
            global_max=Math.max(global_max,local_max);
        }
        
        //return the global max in the array not the last element
        return global_max;
    }
}
