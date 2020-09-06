class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        elif target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            left = nums[0]
            right = nums[-1]
            ind = int(len(nums)/2)
            #dis = len(nums) - ind
            while (nums.index(right)-nums.index(left)) != 1:
                if target <= nums[ind]:
                    right = nums[ind]
                else:
                    left = nums[ind]
                ind = int((nums.index(right)+nums.index(left))/2)
            return nums.index(right)

