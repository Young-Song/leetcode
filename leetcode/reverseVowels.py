class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        left = 0
        right = len(s)-1
        s= list(s)
        while left<=right:
            if not self.isVowel(s[left]):
                left+=1
                continue
            if not self.isVowel(s[right]):
                right-=1
                continue
            # swap two char and increment/decrement left/right
            temp = s[left]
            s[left]=s[right]
            s[right]=temp
            left+=1
            right-=1
        return "".join(s)
    # note that upper case vowels are also included    
    def isVowel(self,c):
        return c in ['a','e','i','o','u','A','E','I','O','U']
