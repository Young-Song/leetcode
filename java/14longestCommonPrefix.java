public class Solution {
    /**
     * @param strs: A list of strings
     * @return: The longest common prefix
     */
    public String longestCommonPrefix(String[] strs) {
        // write your code here
        if(strs==null||strs.length==0){
            return "";
        }
        
        String shortest = strs[0];
        for(int i=0;i<shortest.length();i++){
            for(int j=1;j<strs.length;j++){
                if(strs[j]==null||strs[j].length()==0){
                    return "";
                }
                if(shortest.charAt(i)!=strs[j].charAt(i)){
                    return shortest.substring(0,i);
                }
            
            }
            
        }
        
        return shortest;
    }
}
