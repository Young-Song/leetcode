class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack=[]
        self.outStack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        elem = None
        if len(self.outStack) > 0:
            elem = self.outStack.pop()
        else:
            while len(self.inStack)>0:
                self.outStack.append(self.inStack.pop())
            elem =self.outStack.pop()
            
        return elem
                
    def peek(self):
        """
        :rtype: int
        """
        if len(self.outStack) >0:
            return self.outStack[-1]
        else:
            while len(self.inStack) >0:
                self.outStack.append(self.inStack.pop())
            return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.inStack)+len(self.outStack)==0
