public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<String>();
        String candidate = new String();
        // use two counters to keep the number of remaining parenthese 
        int left =n;
        int right =n;
        dfs(result, candidate, left, right);
        return result;
    }
    
    public void dfs(List<String> result, String candidate, int left, int right){
        //add too many right parent to string, must be invalid
        if(left>right){
            return;
        }
        //used all left and right parent
        if(left==0 && right==0){
            result.add(new String(candidate));
            return ;
        }
        
        if(left>0){
            dfs(result,candidate+"(",left-1,right);
        }
        if(right>0){
            dfs(result,candidate+")",left,right-1);
        }
    }
}
