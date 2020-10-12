class Solution(object):
    def minOperations(self, logs):
        operation = []
        for opt in logs:
            if opt == '../':
                if operation != []:
                    operation.pop()
            elif opt == './':
                next
            else:
                operation.append(opt)
        return len(operation)
        
