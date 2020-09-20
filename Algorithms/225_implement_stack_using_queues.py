class MyStack(object):

    def __init__(self):
        self.seq = []
        

    def push(self, x):
        self.seq.append(x)
        

    def pop(self):
        val = self.seq.pop()
        return val
        

    def top(self):
        return self.seq[-1]
        

    def empty(self):
        return self.seq == []
    


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
