class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # one-line solution
        # return ''.join(sorted(s))==''.join(sorted(t))
        
        # use dictionary
        count={}
        if len(s)!=len(t):
            return False
        for c in s:
            if c in count:
                count[c]+=1
            else:
                count[c]=1
        
        count2={}
        for c in t:
            if c in count2:
                count2[c]+=1
            else:
                count2[c]=1
        return count==count2
