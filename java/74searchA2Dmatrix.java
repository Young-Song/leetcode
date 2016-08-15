public class Solution {
    /**
     * @param matrix, a list of lists of integers
     * @param target, an integer
     * @return a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if(matrix==null||matrix.length==0||matrix[0].length==0){
            return false;
        }
		// the trick is to find the row        
        int m = matrix.length;
        int n = matrix[0].length;
        int left = 0;//starting row
        int right = m-1;//ending row
        int row = left;
        // search for the row 
		// since left is the first row to search, and right is the last row to search, when they are equal we found the row.
        while(left<right){
            int mid = (left+right)/2;
            if(matrix[mid][0]<=target){
                left=mid;
                // two cases: in row mid or not
				// this is still linear because left is set to mid first
                if(matrix[mid][n-1]>=target){
                    break;
                }
                else{
                    left++;
                }
            }
            if(matrix[mid][0]>target){
                right=mid-1;
            }
        }
        row = left;
        
        
        
        // search in the row
        int col = 0;
        left = 0;
        right = n-1;
        while(left<=right){
            int mid = (left+right)/2;
            if(matrix[row][mid]==target){
                return true;
            }
            else if(matrix[row][mid]<target){
                left=mid+1;
            }
            else{
                right=mid-1;
            }
        }
        // not found
        return false;
    }
}

