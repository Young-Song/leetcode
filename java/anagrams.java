public class Solution {
    /**
     * @param strs: A list of strings
     * @return: A list of strings
     */
    public List<String> anagrams(String[] strs) {
        // write your code here
        HashMap<String,Integer> hash = new HashMap<String,Integer>();
        List<String> result = new ArrayList<String>();
        for(int i=0;i<strs.length;i++){
            char[] arr = strs[i].toCharArray();
            Arrays.sort(arr);
            String sorted = new String(arr);
            if(hash.containsKey(sorted)){
                hash.put(sorted,hash.get(sorted)+1);
            }
            else{
                hash.put(sorted,1);
            }
        }
        
        for(int i=0;i<strs.length;i++){
            char[] arr = strs[i].toCharArray();
            Arrays.sort(arr);
            String sorted = new String(arr);
            if(hash.containsKey(sorted)){
                if(hash.get(sorted)>1){
                    result.add(strs[i]);
                }
            }
        }

        return result;
    }
}
