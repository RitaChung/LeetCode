class Solution(object):
    def findDuplicates(self, nums):
        res = {}
        for i in nums:
            if i in res:
                res[i] = res[i] + 1
            else:
                res[i] = 1
        return ([i for i, v in res.items() if v > 1])
