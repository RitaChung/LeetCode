class Solution(object):
    def twoSum (self, nums, target):
        run = 0
        while run < len(nums):
            init = nums[run]
            init_index = nums.index(init)
            makeup = target - init
            if init == makeup:
                if nums.count(init) >= 2:
                    makeup_index = nums[init_index+1:].index(makeup)+init_index+1
                    break
                else:
                    next
            else:
                if makeup in nums:
                    makeup_index = nums.index(makeup)
                    break
            run += 1
        return [init_index, makeup_index]
