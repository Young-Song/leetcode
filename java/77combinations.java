public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> elem = new ArrayList<Integer>();
        DFS(n,k,result,elem,1);
        return result;
    }
    
    public static void DFS(int n, int k, List<List<Integer>> result, List<Integer> elem, int idx){
        if(elem.size()==k){
            result.add(new ArrayList<Integer>(elem));
            return;
        }
        if(elem.size()>k || idx>n){
            return ;
        }
        for(int i=idx;i<=n;i++){
            elem.add(i);
            DFS(n,k,result,elem,i+1);
            elem.remove(elem.size()-1);
        }
    }
}
