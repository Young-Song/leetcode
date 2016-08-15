class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        //write your code here
        if(nums==null||nums.length==0){
            return -1;
        }
        int best = nums.length;
        int left = 0;//starting 
        int right = nums.length-1;//ending
        while(left<=right){
            int mid = (left+right)/2;
            if(target==nums[mid]){
                if(best>mid){
                    best=mid;
                }
                //two cases: left < mid  or left == mid
                // if left < mid, set right =mid-1 and keep searching [left,right]
                // if left==mid, right = mid -1, right<left, best is set above.
                // out of loop
                right=mid-1;
            }
            else if(target<nums[mid]){
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }
        
        return best==nums.length?-1:best;
    }
}
