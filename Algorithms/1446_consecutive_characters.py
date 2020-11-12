class Solution(object):
    def maxPower(self, s):
        cum = 1
        max = 0
        for pos in range(len(s)):
            if pos != 0:
                if s[pos] == s[pos-1]:
                    cum += 1
                else:
                    if cum > max:
                        max = cum
                    cum = 1
        if cum > max:
            max = cum
        return max
