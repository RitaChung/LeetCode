class Solution(object):
    def removeElement(self, nums, val):
        if val in nums:
            for i in range(nums.count(val)):
                nums.remove(val)
        return len(nums)
