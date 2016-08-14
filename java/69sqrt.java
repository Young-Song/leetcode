class Solution {
    /**
     * @param x: An integer
     * @return: The sqrt of x
     */
    public int sqrt(int x) {
        // write your code here
        if(x<0){
            return -1;
        }
        if(x<2){
            return x; 
        }
        int left = 1;
		// only consider [1,x/2]
        int right = x/2;
        int n = (left+right)/2;
        while(true){
            n = (left+right)/2;
            if(n<=x/n && n+1> x/(n+1)){
                break;
            }
			// n*n>x n is too large
            if(n>x/n){
                right=n-1;
            }
			// otherwise n is too small
            else{
                left=n+1;
            }
        }
        
        return n;
    }
}
