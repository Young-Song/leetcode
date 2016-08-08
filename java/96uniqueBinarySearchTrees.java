public class Solution {
    public int numTrees(int n) {
        if(n<2){
            return 1;
        }
        int[] count = new int[n+1];
        count[0]=1;
        count[1]=1;
        for(int i=2;i<n+1;i++){
            //separate j nodes into left and right subtrees
            for(int j=0;j<i;j++){
                count[i]+=count[i-1-j]*count[j];
            }
        }
        return count[n];
    }
}
