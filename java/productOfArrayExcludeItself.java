public class Solution {
    /**
     * @param A: Given an integers array A
     * @return: A Long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    public ArrayList<Long> productExcludeItself(ArrayList<Integer> A) {
        // write your code
        ArrayList<Long> result = new ArrayList<Long>();
        if(A==null||A.size()==0){
            return result;
        }
        //product of A[x] x<=i-1, need to be long
        long[] left = new long[A.size()];
        //product of A[x] x>= i+1
        long[] right = new long[A.size()];
        left[0]=1;
        for(int i=1;i<left.length;i++){
            // multiply A.get(i-1), not A.get(i), implicit casting
            left[i]=left[i-1]*A.get(i-1);
        }
        right[right.length-1]=1;
        for(int j=right.length-2;j>=0;j--){
            right[j]=right[j+1]*A.get(j+1);
        }
        
        for(int i=0;i<A.size();i++){
            result.add(left[i]*right[i]);
        }
        return result;
    }
}

