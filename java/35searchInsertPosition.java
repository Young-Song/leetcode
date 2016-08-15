public class Solution {
    /** 
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
    public int searchInsert(int[] A, int target) {
        // write your code here
        if(A==null||A.length==0){
            return 0;
        }
        //search forward
        for(int i =0;i<A.length;i++){
            if(A[i]>=target){
                return i;
            }
        }
        
        return A.length;
    }
}

