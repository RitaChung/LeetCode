class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max = 0
        cum = 0
        for run in nums:
            if run == 1:
                cum += 1
            else:
                if cum > max:
                    max = cum
                cum = 0
        if cum > max:
            max = cum
        return max
