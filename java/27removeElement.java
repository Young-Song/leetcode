public class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums==null||nums.length==0){
            return 0;
        }
        int tail = 0;
        int right =nums.length-1;
        while(tail<=right){
            if(nums[tail]==val){
                nums[tail]=nums[right];
                right--;
            }
            else{
                tail++;
            }
        }
        return tail;
    }
}
