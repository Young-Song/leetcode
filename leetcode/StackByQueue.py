class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = collections.deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            return 0
        for i in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())
        return self.stack.popleft()
        
       
    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            return 0
        for i in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())
        """
        # NOTE: append the top back
        """
        elem = self.stack.popleft()
        self.stack.append(elem)
        return elem

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack)==0
        
