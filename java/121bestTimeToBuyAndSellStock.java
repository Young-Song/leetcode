public class Solution {
    public int maxProfit(int[] prices) {
        if(prices==null||prices.length==0){
            return 0;
        }
        // min before i
        int[] left_min = new int[prices.length];
        // max after i
        int[] right_max = new int[prices.length];
        
        left_min[0]=prices[0];
        int max_diff = 0;
        for(int i=1;i<prices.length;i++){
            left_min[i] = Math.min(left_min[i-1],prices[i-1]);
            if(max_diff<prices[i]-left_min[i]){
                max_diff=prices[i]-left_min[i];
            }
        }
        
        return max_diff;
    }
}
