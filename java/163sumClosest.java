public class Solution {
    /**
     * @param numbers: Give an array numbers of n integer
     * @param target : An integer
     * @return : return the sum of the three integers, the sum closest target.
     */
    public int threeSumClosest(int[] numbers, int target) {
        // write your code here
        Arrays.sort(numbers);
        int closest = Integer.MAX_VALUE;
        int closest_sum = 0;
        for(int i=0;i<numbers.length-2;i++){
            int left = i+1;
            int right = numbers.length-1;
            while(left<right){
                int sum = numbers[i]+numbers[left]+numbers[right];
                if(sum==target){
                    return target;
                }
                else if(sum<target){
                    if(Math.abs(sum-target)<closest){
                        closest=Math.abs(sum-target);
                        closest_sum=sum;
                    }
                    left++;
                }
                else{
                    if(Math.abs(sum-target)<closest){
                        closest=Math.abs(sum-target);
                        closest_sum=sum;
                    }
                    right--;
                }
            }
        }
        return closest_sum;
    }
}

