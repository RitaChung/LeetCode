class MyQueue(object):

    def __init__(self):
        self.seq = []
        

    def push(self, x):
        self.seq.insert(0,x)
        

    def pop(self):
        val = self.seq.pop()
        return val
        

    def peek(self):
        return self.seq[-1]
        

    def empty(self):
        return self.seq == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
