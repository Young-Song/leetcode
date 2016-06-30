class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result=[]
        candidate=[]
        self.helper(candidates,result,candidate,target,0)
        
        return result
        
    def helper(self,candidates,result,candidate,target,idx):
        if target == 0:
            result.append(candidate[:])
            return 
        if target < 0:
            return 
        # back tracing 
        """
        append the smallest element and test if the target if satisfied.
        if the sum exceed the target, remove the largest element from the list, go back to for loop and try next element in candidates 
        if the sum is exactly the same, add a copy to the result
        if the sum is less than the target, keep adding next element and try
        
        """
        for i in range(idx,len(candidates)):
            candidate.append(candidates[i])
            self.helper(candidates,result,candidate,target-candidates[i],i)
            if  len(candidate)>0:
                del candidate[-1]
        
