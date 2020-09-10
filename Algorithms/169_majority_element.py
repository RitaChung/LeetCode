class Solution(object):
    def majorityElement(self, nums):
        init = list(set(nums))
        threshold = len(nums)/2
        run = 0
        while run < len(init):
            if nums.count(init[run]) > threshold:
                return init[run]
            else:
                run += 1
