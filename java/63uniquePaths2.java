public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        if(m==0||n==0){
            return 0;
        }
        
        int[][] paths = new int[m][n];
        
        //if the initial point is invalid. there are no path at all
        if(obstacleGrid[0][0]==1){
            return 0;
        }
        
        //initialization
        paths[0][0]=1;
        for(int i=1;i<m;i++){
            //check each entry, if there is an obstacle, then no path
            //otherwise, one path from its neighbor on the edge
            if(obstacleGrid[i][0]!=1){
                paths[i][0]=paths[i-1][0];
            }
            else{
                paths[i][0]=0;
            }
        }
        
        for(int j=1;j<n;j++){
            if(obstacleGrid[0][j]!=1){
                paths[0][j]=paths[0][j-1];
            }
            else{
                paths[0][j]=0;                
            }
        }
        
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                //if obstacle, then no path
                if(obstacleGrid[i][j]==1){
                    paths[i][j]=0;
                }
                else{
                    paths[i][j]=paths[i-1][j]+paths[i][j-1];
                }
            }
        }
        
        return paths[m-1][n-1];
    }
}
