class Solution(object):
    def buildArray(self, target, n):
        cur_target = target
        operation = []
        for num in range(1,n+1):
            operation.append('Push')
            if num == cur_target[0]:
                cur_target.pop(0)
            else:
                operation.append('Pop')

            if cur_target == []:
                break
        return operation
