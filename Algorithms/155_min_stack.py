class MinStack(object):

    def __init__(self):
        self.seq = []
        

    def push(self, x):
        self.seq.append(x)
        

    def pop(self):
        self.seq.pop()
        

    def top(self):
        return self.seq[-1]
        

    def getMin(self):
        val = None
        for i in range(len(self.seq)):
            if i == 0:
                val = self.seq[i]
            else:
                if self.seq[i] < val:
                    val = self.seq[i]
        return val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
