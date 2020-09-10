class Solution(object):
    def containsDuplicate(self, nums):
        init = list(set(nums))
        if len(init) == len(nums):
            return False
        else:
            return True
