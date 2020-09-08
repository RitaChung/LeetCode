class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()
        tag = []
        for i in range(len(nums)):
            if i != 0:
                if nums[i] == nums[i-1]:
                    tag.append(nums[i])
        for i in range(len(tag)):
            remove_ind = nums.index(tag[i])
            nums.pop(remove_ind)
           
        return len(nums)
