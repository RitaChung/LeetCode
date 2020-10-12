class Solution(object):
    def calPoints(self, ops):
        score = []
        for op in ops:
            if op == '+':
                num = score[-1] + score[-2]
                score.append(num)
            elif op == 'C':
                score.pop()
            elif op == 'D':
                num = score[-1] * 2
                score.append(num)
            else:
                score.append(int(op))
        return sum(score)
