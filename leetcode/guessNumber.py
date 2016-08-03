# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        upper = n
        lower= 1
        while True:
            g = (upper+lower)/2
            if guess(g)==0:
                return g
            elif guess(g)<0:
                upper=g-1
            else:
                lower=g+1
        return -1
