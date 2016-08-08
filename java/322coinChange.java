public class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount==0)
            return 0;
        //count[i] minimum number to make change of i
        //count[0] = 0 
        int[] count = new int[amount+1];
        for(int i=1;i<count.length;i++){
            count[i]=Integer.MAX_VALUE;
        }
        
        for(int i=1;i<amount+1;i++){
            int min =Integer.MAX_VALUE;
            for(int c: coins){
                if(c<=i){
                    min = Math.min(min,count[i-c]);
                }
            }
            if(min!=Integer.MAX_VALUE)
                count[i]=min+1;
        }
        return count[amount]==Integer.MAX_VALUE?-1:count[amount];
    }
}
