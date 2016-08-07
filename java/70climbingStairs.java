public class Solution {
    public int climbStairs(int n) {
        if(n<2){
            return 1;
        }
        int[] steps = new int[n+1];
        steps[0]=1;
        steps[1]=1;
        for(int i=2;i<=n;i++){
            steps[i]=steps[i-1]+steps[i-2];
        }
        return steps[steps.length-1];
    }
}
