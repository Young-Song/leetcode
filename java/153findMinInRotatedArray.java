public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        // write your code here
        if(nums==null||nums.length==0){
            return 0;
        }
        
        int min = Integer.MIN_VALUE;
        int left =0;
        int right = nums.length-1;
        while(left<=right){
            int mid = (left+right)/2;
            // even if there is no duplicate, 
            // we use <= because left can be equal to right 
            // then left == mid && mid == right
            if(nums[left]<=nums[mid] && nums[mid]<=nums[right]){
                return nums[left];
            }
            if(nums[mid]<nums[right] && nums[right]<nums[left]){
                right=mid;
            }
            else if(nums[right]<nums[left] && nums[left]<=nums[mid]){
                left=mid+1;
            }
        }
        
        return -1;
    }
}
