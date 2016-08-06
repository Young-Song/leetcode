public class Solution {
    public boolean exist(char[][] board, String word) {
        int row = board.length;
        int col = board[0].length;
        boolean[][] used = new boolean[row][col];
        boolean result = false;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
            if(search(board, used, i,j, 0, word))
                return true;
            }    
        }                
        return false;    
    }

    private boolean search(char[][] board, boolean[][] used, int x, int y, int z, String word){
        int row = board.length;
        int col = board[0].length;
        if(z>=word.length())
            return false;
        if(x<0||y<0||x==row||y==col)
            return false;
        if(used[x][y])
            return false;
        if(board[x][y]!=word.charAt(z))
            return false;
        if(word.length()-1==z)
            return true;
        used[x][y]=true;
        boolean result = search(board, used, x+1, y, z+1 , word) || search(board, used, x-1, y, z+1 , word) || search(board, used, x, y+1, z+1 , word) || search(board, used, x, y-1, z+1 , word);
        used[x][y]=false;
        
        return result;
        
    }
}
