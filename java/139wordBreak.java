public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        boolean[] breakable = new boolean[s.length()+1];
        breakable[0]=true;
        //dp approach
        for(int end =1;end<=s.length();end++){
            for(int start=0;start<end;start++){
                String word = s.substring(start,end);
                if(breakable[start] && wordDict.contains(word)){
                    breakable[end]=true;                    
                }                
            }
        }
        
        return breakable[s.length()];
    }
}
