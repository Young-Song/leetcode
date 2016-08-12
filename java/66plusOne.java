public class Solution {
    public int[] plusOne(int[] digits) {
        if(digits==null||digits.length==0)
            return digits;
        int carry =1;
        for(int i=digits.length-1;i>=0;i--){
            int digit = (digits[i]+carry)%10;
            carry = (digits[i]+carry)/10;
            digits[i]=digit;
            if(carry == 0){
                return digits;
            }
        }
        //if the first bit is 1, then the rest must be zeros
        int[] nums = new int[digits.length+1];
        nums[0]=1;
        return nums;
    }
}
