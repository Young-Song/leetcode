public class Solution {
    public int findPeakElement(int[] nums) {
        if(nums==null||nums.length==0){
            return -1;
        }
        
        int left = 0;
        int right = nums.length-1;
        while(left<=right){
            //boundary cases
            int mid = (left+right)/2;
            if((mid-1<0 || nums[mid]> nums[mid-1]) && (mid+1==nums.length ||nums[mid]>nums[mid+1])){
                return mid;
            }
            if(mid-1>=0 && nums[mid-1]>nums[mid]){
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }
        return -1;
    }
}
