class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        index = len(digits)-1
        result= [0]*(index+2)
        while(index>=0):
            d = carry + digits[index]
            if d==10:
                carry=1
                d=0
            else:
                carry=0
            result[index+1]=d
            index-=1
        
        if carry ==1:
            result[0]=1
            return result
        else:
            return result[1:]
        
