class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>=10:
            n = self.addDigit(n)
		# mod 7 ==0
        return n==1 or n==7
    
    def addDigit(self,n):
        if n<10:
            return int(math.pow(n,2))
        else:
            return int(math.pow(n%10,2))+int(self.addDigit(n/10))
