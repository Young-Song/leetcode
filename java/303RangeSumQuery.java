public class NumArray {
    // sums[i] store summation from nums[0] to nums[i]
    int[] sums;
    public NumArray(int[] nums) {
        if(nums==null||nums.length==0){
            sums=null;
            return;
        }
        sums = new int[nums.length];
        sums[0]=nums[0];
        for(int i=1;i<sums.length;i++){
            sums[i]=nums[i]+sums[i-1];
        }
    }

    public int sumRange(int i, int j) {
        // check if sums is valid, if not, return 0
        if(sums==null){
            return 0;
        }
        
        if(i==0){
            return sums[j];
        }
        return sums[j]-sums[i-1];
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
