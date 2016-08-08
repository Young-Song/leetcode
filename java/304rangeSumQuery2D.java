public class NumMatrix {
    int[][] sums;
    public NumMatrix(int[][] matrix) {
        if(matrix==null||matrix.length==0||matrix[0].length==0){
            return ;
        }
        int m= matrix.length;
        int n= matrix[0].length;
        sums= new int[m][n];
        
        sums[0][0]=matrix[0][0];
        for(int i=1;i<m;i++){
            sums[i][0]=sums[i-1][0]+matrix[i][0];
        }
        for(int j=1;j<n;j++){
            sums[0][j]=sums[0][j-1]+matrix[0][j];   
        }
        
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                sums[i][j]=sums[i-1][j]+sums[i][j-1]-sums[i-1][j-1]+matrix[i][j];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        //startin at the corner 
        if(row1==0 && col1==0){
            return sums[row2][col2];
        }
        //one edge
        else if(row1==0 && col1!=0){
            return sums[row2][col2]-sums[row2][col1-1];
        }
        else if(row1!=0 && col1==0){
            return sums[row2][col2]-sums[row1-1][col2];
        }
        //general case - no edge
        else{
            return sums[row2][col2]-sums[row1-1][col2]-sums[row2][col1-1]+sums[row1-1][col1-1];
        }
    }
}


// Your NumMatrix object will be instantiated and called as such:
// NumMatrix numMatrix = new NumMatrix(matrix);
// numMatrix.sumRegion(0, 1, 2, 3);
// numMatrix.sumRegion(1, 2, 3, 4);
