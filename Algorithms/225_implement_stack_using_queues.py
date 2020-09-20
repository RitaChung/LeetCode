class MyStack(object):

    def __init__(self):
        self.squ = []
        

    def push(self, x):
        self.squ.append(x)
        

    def pop(self):
        val = self.squ.pop()
        return val
        

    def top(self):
        return self.squ[-1]
        

    def empty(self):
        return self.squ == []
    


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
