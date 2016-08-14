public class Solution {
    /**
     * @param numbers : Give an array numbers of n integer
     * @return : Find all unique triplets in the array which gives the sum of zero.
     */
    public ArrayList<ArrayList<Integer>> threeSum(int[] numbers) {
        // write your code here
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if(numbers==null||numbers.length==0){
            return result;
        }
        Arrays.sort(numbers);
        
        for(int i=0;i<numbers.length-2;i++){
            if(i>0 && numbers[i]==numbers[i-1])
                continue;
            int first = i;
            int left = i+1;
            int right = numbers.length-1;
            while(left<right){
                int sum = numbers[first]+numbers[left]+numbers[right];
                if(sum==0){
                    ArrayList<Integer> elem = new ArrayList<Integer>();
                    elem.add(numbers[first]);
                    elem.add(numbers[left]);
                    elem.add(numbers[right]);
                    result.add(elem);
                    left++;
                    right--;
                    while(left<right && numbers[left]==numbers[left-1])
                        left++;
                    while(left<right  && numbers[right]==numbers[right+1])
                        right--;
                }
                else if(sum<0){
                    left++;
                }
                else{
                    right--;
                }
            }
            
        }
        return result;
    }
}
