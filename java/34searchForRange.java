public class Solution {
    /** 
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
    public int[] searchRange(int[] A, int target) {
        // write your code here
        // two binary search, one for start, the other for end
        int[] result = {-1,-1};
        if(A==null||A.length==0){
            return result;
        }
        
        int left = 0;
        int right = A.length-1;
        int start = A.length;
        while(left<=right){
            int mid = (left+right)/2;
            if(A[mid]==target){
                start=mid;
                right=mid-1;
            }
            else if(A[mid]<target){
                left=mid+1;
            }
            else{
                right=mid-1;
            }
        }
        
        // not found
        if(start==A.length){
            return result;
        }
        result[0]=start;
        left =0;
        right =A.length-1;
        int end = -1;
        while(left<=right){
            int mid = (left+right)/2;
            if(A[mid]==target){
                end=mid;
                left=mid+1;
            }
            else if(target<A[mid]){
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }
        result[1]=end;
        return result;
    }
}

